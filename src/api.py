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
        """Метод получения вакансий с НeadHunter"""

        url = 'http://api.hh.ru/vacancies'
        file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        params = {
            'text': f'name:{query_vacancy}',  # Текст фильтра
            'page': 1,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            # Получаем данные из ответа в формате JSON
            data = response.json()['items']

            vacancy_list = []

            for item in data:
                if item['salary']:
                    if item['salary']['from'] and item['salary']['to']:

                        item_dict = {'vacancy_title': item['name'],
                                     'vacancy_link': item['alternate_url'],
                                     'vacancy_city': item['area']['name'],
                                     'company_name': item['employer']['name'],
                                     'salary_from': item['salary']['from'],
                                     'salary_to': item['salary']['to'],
                                     'vacancy_responsibility': item['snippet']['responsibility'],
                                     'vacancy_requirements': item['snippet']['requirement']
                                     }
                        vacancy_list.append(item_dict)

            with open(file_json, 'w', encoding='utf-8') as file:
                json.dump(vacancy_list, file, indent=4, ensure_ascii=False)

            return vacancy_list

    def read_file(self):
        file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
