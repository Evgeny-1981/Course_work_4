import json
import requests
import time
from datetime import datetime
import os
from config import DATA_PATH
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Создаем абстрактный класс"""

    @abstractmethod
    def __init__(self):
        pass
    #
    # @abstractmethod
    # def __str__(self):
    #     pass
    #
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
        return f'Осуществляется подключение класса {self.__class__.__name__} HH для получения вакансии'

    def get_vacancy(self, query_vacancy):
        """Получаем вакансии с HH"""
        vacancy_list = []
        t_date = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
        FILE = os.path.join(DATA_PATH, f'Vavancy_{t_date}.json')
        params = {
            'text': f'name:{query_vacancy}',  # Текст фильтра.
            'page': 10,  # Индекс страницы поиска на HH
            'per_page': 30  # Кол-во вакансий на 1 странице
        }
        response = requests.get(url=self.url, params=params)
        vacancy_list = (json.loads(response.text)['items'])
        with open(FILE, 'w') as file:
            json.dump(vacancy_list, file, indent=2, ensure_ascii=False)

        return vacancy_list


