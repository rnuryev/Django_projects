from django.db import models
import requests
from bs4 import BeautifulSoup
from datetime import date
from django.shortcuts import get_object_or_404

class RzdTenders(models.Model):

    url = models.CharField(max_length=250, default='http://etzp.rzd.ru/freeccee/main?ACTION=searchProc')
    query_string = models.CharField(max_length=250)
    #bid_deadlin_from = models.DateField(default=date.today, null=True, blank=True)
    bid_deadlin_from = models.CharField(max_length=50)

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
            # total_page = int(soup.find('div', class_='a8b').find_all('td', class_='pagesButtons')[-1].text.strip())
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

            return data

        data = {
            'p_page': 0,
            'p_page_size': 900,
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
            'name_text': self.query_string,
            'p_dateend_begin': self.bid_deadlin_from,
            'p_dateend_begin_old': self.bid_deadlin_from,
            'p_dateend_end': None,
            'p_dateend_end_old': None,
            'p_contest_date_oa_begin_old': None,
            'p_contest_date_oa_end_old': None,
        }

        all_links = get_all_links(self.url, data)

        for link in all_links:
            data_tender = get_page_data(link)
            new_tender = Tenders(code=data_tender['code'],
                                 subject=data_tender['subject'],
                                 customer=data_tender['customer'],
                                 price=data_tender['price'],
                                 deadline=data_tender['deadline'],
                                 link=data_tender['link'])

            new_tender.rzd_tenders_request = RzdTenders.objects.get(pk=self.pk)

            new_tender.save()

            for doc_l in data_tender['document_links']:
                new_tender_documents = TenderDocuments(doc_title=doc_l['doc_name'], doc_link=doc_l['doc_link'])
                new_tender_documents.tender = new_tender
                new_tender_documents.save()



class Tenders(models.Model):
    code = models.CharField(max_length=100)
    subject = models.CharField(max_length=350)
    customer = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    deadline = models.CharField(max_length=20)
    link = models.URLField()
    rzd_tenders_request = models.ForeignKey(RzdTenders, related_name='found_tenders', on_delete=models.CASCADE)


class TenderDocuments(models.Model):
    doc_title = models.CharField(max_length=250)
    doc_link = models.URLField()
    tender = models.ForeignKey(Tenders, related_name='document_links', on_delete=models.CASCADE)





