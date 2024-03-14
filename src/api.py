import json
import requests
import time
from datetime import datetime
import os
from config import VACANCY_FILE, DATA_PATH
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Создаем абстрактный класс"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancy(self, query):
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.url = 'http://api.hh.ru/vacancies'

    def __repr__(self):
        return f'Осуществляется подключение класса {self.__class__.__name__} к сайту HH для получения вакансии'

    def get_vacancy(self, query_vacancy):
        """Получаем вакансии с HH"""
        vacancy_list = []
        t_date = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
        FILE = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        params = {
            'text': f'name:{query_vacancy}',  # Текст фильтра
            'page': 10,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = requests.get(url=self.url, params=params)
        vacancy_dict = response.json()
        # print(type(vacancy_dict))
        vacancy_list = json.loads(response.text)['items']
        # print(type(vacancy_list))
        with open(FILE, 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)
        vacancy = response.json()

        # for c in vacancy:
        #     return c
            # print(c)
            # c_items = c.get('items')
            # c_name = c.get(['name'])
        #
        #     for item in c_items:
        #         item_name = item.get('name')
        #         # item_salary = item.get('salary')
        #     # json.dump(vacancy_list, file, indent=4, ensure_ascii=False)
        #     vacancy_list.append([c_name, item_name])
        return vacancy_list

    def read_file(self):
        with open(VACANCY_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # print(type(data))
        return data



