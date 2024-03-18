import requests
import os
import csv
import json
from datetime import datetime
from config import DATA_PATH
from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def main():
    query_vacancy = input("Какую вакансию будем искать? ")
    # other_params = input("Желаете уточнить параметры поиска? (Да(Y)/Нет(N)")
    # if other_params.lower() == "Y":
    #     query_city = input("В каком городе? ")
        # query_salary = input("Начальный уровень зарплаты? ")
        # query_n_vacancy = input("Сколько вакансий вывести? ")

    hh_api = HeadHunterAPI()
    print(repr(hh_api))
    hh_vacancy = hh_api.get_vacancy(query_vacancy)

    # for item in hh_vacancy:
    #     if isinstance(item['salary_from'], int):
    sorted_vacancy = sorted(hh_vacancy, key=lambda x: x['salary_from'], reverse=True)

    for item in sorted_vacancy[:5]:
        print(item)


if __name__ == '__main__':
    main()
