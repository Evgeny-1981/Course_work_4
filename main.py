import requests
import os
import csv
import json
from datetime import datetime
from config import DATA_PATH
from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def main():
    vacancy_list = []
    query_vacancy = input("Какую вакансию будем искать? ")
    # query_city = input("В каком городе? ")
    query_salary = input("Начальный уровень зарплаты? ")
    # query_n_vacancy = input("Сколько вакансий ввести? ")
    hh_api = HeadHunterAPI()
    print(repr(hh_api))
    hh_vacancy = hh_api.get_vacancy(query_vacancy)
    # print(type(hh_vacancy))
    for n in hh_vacancy:
        if isinstance(n['salary'], dict):
            name = n.get('name')
            salary = n.get('salary')
            if salary.get('from'):
                salary_from = salary.get('from')
            if salary.get('to'):
                salary_to = salary.get('to')
            # print(name, salary_from, salary_to)
            vacancy_list.append(name)
            v = Vacancy('name', 'salary_from')

    print(vacancy_list)
    print(len(vacancy_list))

    # v = hh_api.read_file()
    # for i in v:
    #     if isinstance(i['salary'], dict):
    #         if i['salary']['from'] >= int(query_salary):# and i['salary']['to']:
    #
    #             print(f'{i['salary']['from']}')# - {i['salary']['to']}')
    #     # print(i['name'], i['salary'])


if __name__ == '__main__':
    main()
