import psycopg2

def delete_old_tenders():
    with psycopg2.connect(dbname='tenders', user='postgres', password='1Qwerty', host='127.0.0.1', port='5432') as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM public.tenders_tenders WHERE deadline < current_date AND NOT EXISTS (SELECT * FROM public.tenders_favoritetenders WHERE fav_tender_id = public.tenders_tenders.id)")
            conn.commit()

if __name__ == '__main__':
    delete_old_tenders()
