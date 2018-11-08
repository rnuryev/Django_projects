from PythonScripts import gazprom_parser as gaz_parse
from PythonScripts import rosatom_parser as ros_parse
from PythonScripts import rosseti_parser as seti_parse
from PythonScripts import rzd_parser_save_in_DB as rzd_parse
import time
import datetime


if __name__ == '__main__':
    with open('log.txt', 'a') as f:
        f.write('Парсинг Газпром. Начало: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
    gaz_parse.run_it()
    with open('log.txt', 'a') as f:
        f.write('Парсинг Газпром. Завершение: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
    time.sleep(300)
    with open('log.txt', 'a') as f:
        f.write('Парсинг Росатом. Начало: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
    ros_parse.run_it()
    with open('log.txt', 'a') as f:
        f.write('Парсинг Росатом. Завершение: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
    time.sleep(300)
    with open('log.txt', 'a') as f:
        f.write('Парсинг Россети. Начало: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
    seti_parse.run_it()
    with open('log.txt', 'a') as f:
        f.write('Парсинг Россети. Завершение: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
    time.sleep(300)
    with open('log.txt', 'a') as f:
        f.write('Парсинг РЖД. Начало: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
    rzd_parse.run_it()
    with open('log.txt', 'a') as f:
        f.write('Парсинг РЖД. Завершение: ' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n')
