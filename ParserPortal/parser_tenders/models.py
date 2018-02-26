from django.db import models
import requests
from bs4 import BeautifulSoup


# Create your models here.

class Rzd_Parser(models.Model):
    URL_BASE = 'http://tender.rzd.ru/tender/public/ru?cod=&deal_type=&property_type_id=&organaizer_id=&city_id=&status_type=1&name='
    URL_ADDIT_PART = '&date_from=&date_to=&action=filtr&STRUCTURE_ID=4078&layer_id=&x=31&y=12'
    URL_PAGE_PART = '&page4893_1465='
    date = models.DateField()
    code = models.CharField(max_length=50)
    subject = models.CharField(max_length=250)
    link = models.CharField(max_length=500)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.subject


    def get_html(url):
        r = requests.get(url)
        return r.text


    def get_total_pages(html):
        soup = BeautifulSoup(html, 'lxml')
        pages = soup.find('div', class_='padB10').find_all('a')[-1].get('href')
        total_pages = int(pages[-1])
        return total_pages


    def get_page_data(html):
        soup = BeautifulSoup(html, 'lxml')
        tenders = soup.find('table', class_='table').find_all('tr')
        for tender in tenders:
            tds = tender.find_all('td')
            try:
                date = tds[1].text.strip()
            except:
                date = ''
            try:
                code = tds[2].text.strip()
            except:
                code = ''
            try:
                sls = tds[5].find('a').text.split('\n')
                subject = ' '.join(list(map(str.strip, sls)))
            except:
                subject = ''
            try:
                link = 'http://tender.rzd.ru' + tds[5].find('a').get('href')
            except:
                link = ''
            data = {'date': date,
                    'code': code,
                    'subject': subject,
                    'link': link}

            # write_csv(data)

