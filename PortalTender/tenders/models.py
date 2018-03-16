from django.db import models
import requests
from bs4 import BeautifulSoup
from datetime import date

class Tenders(models.Model):
    code = models.CharField(max_length=100)
    subject = models.CharField(max_length=350)
    customer = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    deadline = models.DateTimeField()
    link = models.URLField()
    rzd_tenders_request = models.ForeignKey(RzdTenders, related_name='found_tenders')


class TenderDocuments(models.Model):
    doc_title = models.CharField(max_length=250)
    doc_link = models.URLField()
    tender = models.ForeignKey(Tenders, related_name='document_links')

class RzdTenders(models.Model):
    DATA_SET = {
        'p_page': 0,
        'p_page_size': 25,
        'p_order': 'DATEENDSEARCH',
        'p_orderType': 'DESC',
        'p_org': 'all',
        'p_cust': 'all',
        'p_inlots': 'true',
        'p_msp': 'false',
        'p_type_select': None,
        'p_cust_select': 'all',
        'p_org_select': 'all',
        'p_cnumber': None,
        # 'name_text': name_text,
        # 'p_dateend_begin': bid_deadlin_from,
        # 'p_dateend_begin_old': bid_deadlin_from,
        'p_dateend_end': None,
        'p_dateend_end_old': None,
        'p_contest_date_oa_begin_old': None,
        'p_contest_date_oa_end_old': None,
    }
    url = models.CharField(max_length=250, default='http://etzp.rzd.ru/freeccee/main?ACTION=searchProc')
    query_string = models.CharField(max_length=250)
    bid_deadlin_from = models.DateField(default=date.today)

    def __str__(self):
        return 'Тендеры РЖД. Запрос: ' + self.query_string

    def get_tenders(self):

        def get_html_post(url, data):
            r = requests.post(url, data=data)
            return r.text

        def get_html_get(url):
            r = requests.get(url)
            return r.text

        def get_all_links(url, data):
            html = get_html_post(url, data)
            soup = BeautifulSoup(html, 'lxml')
            links = soup.find('table', class_='tableProc').find_all('tr')
            all_links = []
            for lk in links:
                if lk.has_attr('onclick'):
                    link = 'http://etzp.rzd.ru' + lk['onclick'][10:len(lk['onclick']) - 3]
                    all_links.append(link)
            return all_links

        def get_page_data(url):
            html = get_html_get(url)
            soup = BeautifulSoup(html, 'lxml')

            spans_tender_info = soup.find('table', id='descriptionTable').find_all('span')

            try:
                code = spans_tender_info[0].text.strip()
            except:
                code = ''
            try:
                subject = spans_tender_info[1].text.strip()
            except:
                subject = ''
            try:
                customer = spans_tender_info[2].text.strip()
            except:
                customer = ''
            try:
                price = spans_tender_info[4].text.strip()
            except:
                price = ''
            try:
                deadline = spans_tender_info[6].text.strip()
            except:
                deadline = ''
            try:
                link = url
            except:
                link = ''
            try:
                document_links = []
                trs_a = soup.find('div', id='attachmentsDiv').find('table').find_all('a')
                for tr in trs_a:
                    dl = {}
                    dl['doc_name'] = tr.text.strip()
                    dl['doc_link'] = 'http://etzp.rzd.ru' + tr.get('href')
                    document_links.append(dl)
            except:
                document_links = []
            data = {
                'code': code,
                'subject': subject,
                'customer': customer,
                'price': price,
                'deadline': deadline,
                'link': link,
                'document_links': document_links
            }

            write_csv(data)