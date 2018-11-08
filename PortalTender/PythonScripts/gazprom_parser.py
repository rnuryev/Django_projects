import requests
import datetime
import psycopg2
import json
from multiprocessing import Pool

requests.packages.urllib3.disable_warnings()

def write_db(data):
    with psycopg2.connect(dbname='tenders', user='postgres', password='1Qwerty', host='127.0.0.1', port='5432') as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM public.tenders_tenders WHERE code=%s", (data['code'],))
            result = cur.fetchall()
            if not result:
                cur.execute("INSERT INTO public.tenders_tenders (etp, code, subject, customer, price, deadline, link, lots, document_links, in_favorite) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, FALSE)",
                        (data['etp'], data['code'], data['subject'], data['customer'], data['price'], datetime.datetime.strptime(data['deadline'][0:10], '%Y-%m-%d').date(), data['link'], json.dumps(data['lots']), json.dumps(data['document_links'])))

def get_all_ids():
    page_count = 1
    all_ids = []
    while True:
        url_1 = 'http://www.gazprom.ru/json/site/tender.html?sEcho=' + str(page_count) + '&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=50&mDataProp_0=purchase_type&mDataProp_1=purchase_number&mDataProp_2=company_customer&mDataProp_3=company_org&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&sSearch_2=&bRegex_2=false&bSearchable_2=true&sSearch_3=&bRegex_3=false&bSearchable_3=true&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=true&status=active&lang=ru&limit=50&page=' + str(page_count) + '&sort_field=date&_=152611664629'
        r = requests.get(url=url_1)
        tenders = json.loads(r.text)['tenders']
        if not tenders:
            break
        for i in tenders:
            all_ids.append(i['gpb_id'])
        page_count += 1
    return all_ids

def get_token_cookies():

    data_for_token = {
        "action":"Index",
        "method":"index",
        "data":None,
        "type":"rpc",
        "tid":2,
        "token":""}

    url_for_token = 'https://etpgaz.gazprombank.ru/index.php?rpctype=direct&module=default&client=etp'
    r = requests.post(url=url_for_token, data=data_for_token, verify=False)
    token = json.loads(r.text)['result']['auth_token']
    cookie = r.cookies
    return token, cookie


def get_tender_data(id):

    token1, cookie1 = get_token_cookies()
    url_for_tender = 'https://etpgaz.gazprombank.ru/index.php?rpctype=direct&module=default&client=etp'

    data_for_tender = {"action":"Procedure",
             "method":"load",
             "data":[{
                 "procedure_id":id,
                 "act":None,
                 "change_logo":None,
                 "hide_contact":True}],
             "type":"rpc",
             "tid":3,
             "token":token1}

    resp = requests.post(url=url_for_tender, data=json.dumps(data_for_tender), cookies=cookie1, verify=False)
    tender_json = resp.json()
    try:
        code = tender_json['result']['procedure']['registry_number']
    except:
        code = ''
    try:
        subject = tender_json['result']['procedure']['title']
    except:
        subject = ''
    try:
        customer = tender_json['result']['procedure']['org_full_name']
    except:
        customer = ''
    try:
        # if tender_json['result']['procedure']['lots'][1]['start_price']:
        #     price = ''
        # else:
        price = tender_json['result']['procedure']['lots'][0]['start_price']
    except:
        price = ''
    try:
        deadline = tender_json['result']['procedure']['date_end_registration']
    except:
        deadline = '1900-01-01'
    try:
        link = tender_json['result']['procedure']['url']
    except:
        link = ''
    try:
        document_links = []

        if tender_json['result']['procedure']['common_files']:
            tds = tender_json['result']['procedure']['common_files']
            for i in tds:
                dl = {}
                dl['doc_name'] = i['name']
                dl['doc_link'] = 'https://etpgaz.gazprombank.ru' + i['link']
                document_links.append(dl)
        elif tender_json['result']['procedure']['lots']:
            tds = tender_json['result']['procedure']['lots'][0]['lot_documentation']
            for i in tds:
                dl = {}
                dl['doc_name'] = i['name']
                dl['doc_link'] = 'https://etpgaz.gazprombank.ru' + i['link']
                document_links.append(dl)
        # else:
        #     tender_detail = ''
    except:
        document_links = []
    try:
        lots = []
        all_lots = tender_json['result']['procedure']['lots']
        for index, tl in enumerate(all_lots):
            if tl['subject']:
                temp_dict = {}
                temp_dict['num_lot'] = index + 1
                temp_dict['name_lot'] = tl['subject']
                temp_dict['price_lot'] = tl['start_price']
                lots.append(temp_dict)
    except:
        lots = []
    data = {
        'etp': 'Газпром',
        'code': code,
        'subject': subject,
        'customer': customer,
        'price': price,
        'deadline': deadline,
        'link': link,
        'document_links': document_links,
        'lots': lots
    }

    write_db(data)

def run_it():
    all_ids = get_all_ids()

    with Pool(20) as po:
        po.map(get_tender_data, all_ids)


if __name__ == '__main__':
    run_it()
