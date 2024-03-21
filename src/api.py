import json
import requests
import os
from config import DATA_PATH
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
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancy = []

    def __repr__(self):
        return f'Ожидайте, выполняется подключение класса {self.__class__.__name__} к сайту HH для получения вакансии...\n'

    def get_vacancy(self, query_vacancy):
        """Метод для запроса к HeadHunter для получения вакансий"""

        self.params['text'] = query_vacancy
        vacancy_list = []
        # while self.params.get('page') != 20:
        response = requests.get(f'{self.url}?per_page=100&page=0&text={query_vacancy}&search_field=name') #headers=self.headers, params=self.params')
        vacancy = response.json()['items']
        self.vacancy.extend(vacancy)
        self.params['page'] += 1
        vacancy_list = self.vacancy

        return vacancy_list

    def save_json(self, vacancy_json):
        file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        vacancy_list = []
        for item in vacancy_json:
            if item['salary']:
                salary_from = item['salary']['from']
                salary_to = item['salary']['to']
                if item['salary']['from'] is None:
                    salary_from = 0
                if item['salary']['to'] is None:
                    salary_to = 0
                item_dict = {'vacancy_title': item['name'],
                             'vacancy_link': item['alternate_url'],
                             'vacancy_city': item['area']['name'],
                             'company_name': item['employer']['name'],
                             'salary_from': salary_from,
                             'salary_to': salary_to,
                             'currency': item['salary']['currency'],
                             'vacancy_responsibility': item['snippet']['responsibility'],
                             'vacancy_requirements': item['snippet']['requirement']
                             }
                vacancy_list.append(item_dict)

            with open(file_json, 'w', encoding='utf-8') as file:
                json.dump(vacancy_list, file, indent=4, ensure_ascii=False)

        return vacancy_list


# def read_file(self):
#     file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
#     with open(file_json, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data