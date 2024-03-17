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
    # other_params = input("Желаете уточнить параметры поиска? (Да(Y)/Нет(N)")
    # if other_params.title() == "Y":
    #     query_city = input("В каком городе? ")
    #     query_salary = input("Начальный уровень зарплаты? ")
    #     query_n_vacancy = input("Сколько вакансий вывести? ")

    hh_api = HeadHunterAPI()
    print(repr(hh_api))
    hh_vacancy = hh_api.get_vacancy(query_vacancy)
    hh_vacancy2 = hh_api.read_file()
    result = []
    for i in hh_vacancy2:
        if i['salary']:
            if i['salary']['from'] and i['salary']['to']:
                name = i['name']
                salary_from = i['salary']['from']
                salary_to = i['salary']['to']
                city = i['area']['name']
                employer = i['employer']['name']
                result.append([name, salary_from, salary_to, city, employer])

    file_json = os.path.join(DATA_PATH, f'Vacancy_HH_1.json')
    with open(file_json, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


    # return vacancy
                # for n in result:
                #     print(n)
                # print(name, salary_from, salary_to)
        # else:
        #     print(f'{i['name']}, Зарплата не указана')
        # if isinstance(i['salary'], dict):
        #     print(f'{i['salary']['from']} - {i['salary']['from']}')
    # for n in hh_vacancy:
    #     if isinstance(n['salary'], dict):
    #         name = n.get('name')
    #         salary_from = n.get['salary'].get['from']
    #         salary_to = n.get['salary'].get['to']
    #         # if salary.get('from'):
    #         #     salary_from = salary.get('from')
    #         # if salary.get('to'):
    #         #     salary_to = salary.get('to')
    #         print(name, salary_from, salary_to)
    #         vacancy_list.append(name)
            # v = Vacancy('name', 'salary_from')
    # vac = Vacancy.load_vacancy_from_json()
    # for item in vac:
    #     for i in item:
    #         print(i)
    # print(vacancy_list)
    # print(len(vacancy_list))

    # v = hh_api.read_file()
    # for i in v:
    #     if isinstance(i['salary'], dict):
    #         if i['salary']['from'] >= int(query_salary):# and i['salary']['to']:
    #
    #             print(f'{i['salary']['from']}')# - {i['salary']['to']}')
    #     # print(i['name'], i['salary'])


if __name__ == '__main__':
    main()
