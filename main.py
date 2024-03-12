import requests
import os
import csv
import json
from datetime import datetime


def get_vacancy(name):
    t_date = datetime.now().strftime('%d-%m-%Y')
    params = {
        'text': f'name:{name}',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'page': 1,  # Индекс страницы поиска на HH
        'per_page': 190  # Кол-во вакансий на 1 странице
    }
    response = requests.get(url='https://api.hh.ru/vacancies', params=params)
    with open(f'info_{t_date}.json', 'w') as file:
        json.dump(response.json(), file, indent=2, ensure_ascii=False)

    vacancy = response.json()


def main():
    get_vacancy('Python')



if __name__ == '__main__':
    main()
