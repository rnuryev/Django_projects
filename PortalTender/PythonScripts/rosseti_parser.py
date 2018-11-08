import requests
import datetime
import psycopg2
import json
from datetime import date
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

def get_token_cookies(url, data):
    r = requests.post(url=url, data=data, verify=False)
    token = json.loads(r.text)['result']['auth_token']
    cookie = r.cookies
    return token, cookie


def get_all_tender_links(url, token, ck):

    def get_tenders_links(json_data):
        tenders_links = []
        for i in json_data:
            link = 'https://etp.rosseti.ru/#com/procedure/view/procedure/' + str(i['id'])
            id = i['id']
            data = {
                'link': link,
                'id': id
            }
            tenders_links.append(data)
        return tenders_links


    all_tender_links = []
    start_count = 0
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://etp.rosseti.ru/',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
    }

    date_filter_tenders = datetime.date.today() - datetime.timedelta(days=1)

    while True:
        data_666 = {"action": "Procedure",
                    "method": "list",
                    "data": [{"start": start_count,
                              "limit": 25,
                              "sort": "id",
                              "dir": "DESC",
                              "procedure_type": 0,
                              "status": 2,
                              "organizer": "",
                              "organizer_region": None,
                              "title_like": "",
                              "for_small_or_middle": False,
                              "date_end_registration_from": date_filter_tenders.strftime('%Y-%m-%dT19:00:00.000Z'),
                              "date_end_registration_till": "",
                              "start_price_from": None,
                              "start_price_till": None,
                              "date_begin_auction_from": "",
                              "date_begin_auction_till": "",
                              "customer": "",
                              "department_id": "",
                              "registry_number_like": "",
                              "subcontractors_requirement": False,
                              "query": ""}],
                    "type": "rpc",
                    "tid": 22,
                    "token": token}
        resp = json.loads(requests.post(url=url, data=json.dumps(data_666), headers=head, cookies=ck, verify=False).text)
        test = resp['result']['procedures']
        if not test:
            break
        all_tender_links.extend(get_tenders_links(test))
        start_count = start_count + 25

    return all_tender_links

def get_page_data(url, token, cookie, id):
    data_for_tender_detail = {"action": "Procedure",
                              "method": "load",
                              "data": [{"procedure_id": id,
                                        "is_view": 1,
                                        "act": None}],
                              "type": "rpc",
                              "tid": 17,
                              "token": token}

    resp = json.loads(requests.post(url=url, data=json.dumps(data_for_tender_detail), cookies=cookie, verify=False).text)

    # Ссылки на документы в одной из этих ветвей (необходимо сделать проверку наличия ссылки в перечне документов тенедра, в противном случае делаем исключения

    try:
        code = resp['result']['procedure']['registry_number']
    except:
        code = ''
    try:
        subject = resp['result']['procedure']['title']
    except:
        subject = ''
    try:
        customer = resp['result']['procedure']['org_full_name']
    except:
        customer = ''
    try:
        if resp['result']['procedure']['lots'][1]:
            price = ''
    except:
        price = resp['result']['procedure']['lots'][0]['start_price']
    try:
        deadline = resp['result']['procedure']['date_end_registration']
    except:
        deadline = '1900-01-01'
    try:
        link = resp['result']['procedure']['url']
    except:
        link = ''
    try:
        document_links = []

        if resp['result']['procedure']['common_files']:
            tds = resp['result']['procedure']['common_files']
            for i in tds:
                dl = {}
                dl['doc_name'] = i['name']
                dl['doc_link'] = 'https://etp.rosseti.ru' + i['link']
                document_links.append(dl)
        elif resp['result']['procedure']['lots']:
            tds = resp['result']['procedure']['lots'][0]['lot_documentation']
            for i in tds:
                dl = {}
                dl['doc_name'] = i['name']
                dl['doc_link'] = 'https://etp.rosseti.ru' + i['link']
                document_links.append(dl)
        # else:
        #     tender_detail = ''
    except:
        document_links = []
    try:
        lots = []
        all_lots = resp['result']['procedure']['lots']
        for index, tl in enumerate(all_lots):
            temp_dict = {}
            temp_dict['num_lot'] = index + 1
            temp_dict['name_lot'] = tl['subject']
            temp_dict['price_lot'] = tl['start_price']
            lots.append(temp_dict)
    except:
        lots = []
    data = {
        'etp': 'Россети',
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
    url = 'https://etp.rosseti.ru/index.php?rpctype=direct&module=default'
    data_for_token = {"action": "Index", "method": "index", "data": None, "type": "rpc", "tid": 2, "token": ""}

    token1, ck1 = get_token_cookies(url, data_for_token)

    atl = get_all_tender_links(url, token1, ck1)

    for i in atl:
        get_page_data(url, token1, ck1, i['id'])

if __name__ == '__main__':
    run_it()