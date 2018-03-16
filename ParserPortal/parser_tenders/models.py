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

        #Метод для получения списка тендоров по запросу