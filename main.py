import requests
import os
import csv
import json
from datetime import datetime
from config import DATA_PATH
from src.api import HeadHunterAPI


def main():
    query_vacancy = input("Какую вакансию будем искать? ")
    hh_api = HeadHunterAPI()
    hh_vacancy = hh_api.get_vacancy(query_vacancy)
    # print(hh_api.get_vacancy(query_vacancy))
    n = 1
    for item in hh_vacancy:
        if (item['salary']):
            print(f'{n}. {item['name']}, {item['area']['name']}, {item['alternate_url']}, {item['salary']['from']}-{item['salary']['to']}')
            n += 1


if __name__ == '__main__':
    main()
