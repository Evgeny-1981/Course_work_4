import json
import requests
import os
from config import VACANCY_FILE, DATA_PATH
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Создаем абстрактный класс"""

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancy(self, query):
        pass


class HeadHunterAPI(AbstractAPI):

    def __repr__(self):
        return f'Выполняется подключение класса {self.__class__.__name__} к сайту HH для получения вакансии...'

    def get_vacancy(self, query_vacancy):
        """Функция получения вакансий с НeadHunter"""

        url = 'http://api.hh.ru/vacancies'
        file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        params = {
            'text': f'name:{query_vacancy}',  # Текст фильтра
            'page': 10,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = requests.get(url=url, params=params)
        # vacancy_list = json.loads(response.content)

        with open(file_json, 'w', encoding='utf-8') as file:
            json.dump(response.json()['items'], file, indent=4, ensure_ascii=False)
        vacancy = response.json()['items']

        return vacancy

    def read_file(self):
        file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
