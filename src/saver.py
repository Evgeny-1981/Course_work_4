import json
import os
from abc import ABC, abstractmethod
from config import DATA_PATH


class Saver(ABC):
    """Создаем абстрактный класса рабты с вакансиями"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_json(self, vacancy_json):
        pass

    @abstractmethod
    def add_vacancy(self, sorted_list):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class JSONSaver(Saver):

    def __init__(self):
        self.file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')

    def __repr__(self):
        pass

    def get_json(self, vacancy_json):
        # file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
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

        return vacancy_list

    def save_vacancy(self, filtered_vacancy_list):
        with open(self.file_json, 'w', encoding='utf-8', errors='ignore') as file:
            json.dumps(filtered_vacancy_list, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, filtered_vacancy_list):
        with open(self.file_json, 'a+', encoding='utf-8', errors='ignore') as file:
            json.dump(filtered_vacancy_list, file, indent=4, ensure_ascii=False)

    def del_vacancy(self):
        pass
