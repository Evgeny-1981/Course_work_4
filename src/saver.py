import json
import os
from abc import ABC, abstractmethod
from config import DATA_PATH
from src.vacancy import Vacancy


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
    def save_vacancy(self, sorted_list):
        pass

    @abstractmethod
    def read_vacancy(self):
        pass

    # @abstractmethod
    # def add_vacancy(self, sorted_list):
    #     pass

    @abstractmethod
    def del_vacancy(self):
        pass


class JSONSaver(Saver):

    def __init__(self):
        self.file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        self.file_name = self.file_json
        self.data_json = None
        if not os.path.exists(self.file_json):
            with open(self.file_json, 'w+') as file:
                json.dump(self.data_json, file)
                print(f"Файл {self.file_json} создан")
        self.vacancy_list = []
        self.data = None  # self.read_vacancy()

    def __repr__(self):
        pass

    def get_json(self, vacancy_json):
        """Метод получает список вакансий по запросу и преобразует его в список словарей"""
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
                self.vacancy_list.append(item_dict)

        return self.vacancy_list

    def save_vacancy(self, filtered_vacancy_list):
        """Метод для сохранения вакансий в JSON файл"""
        with open(self.file_json, 'w', encoding='utf-8', errors='ignore') as file:
            json.dump(filtered_vacancy_list, file, indent=4, ensure_ascii=False)
        return filtered_vacancy_list

    def read_vacancy(self):
        """Метод для чтения вакансий из JSON файла"""
        with open(self.file_json, 'r', encoding='utf-8', errors='ignore') as file:
            data = json.load(file)
        return data

    def del_vacancy(self):
        """Метод для удаления вакансий из JSON файла"""
        with open(self.file_json, 'w') as file:
            json.dump(self.data, file)
        # self.data = []
        print("Данные удалены")

    def show_vacancy(self):
        """Метод для отображения вакансий из сохраненньго ранее JSON файла"""
        with open(self.file_json, 'r', encoding='utf-8', errors='ignore') as file:
            data = json.load(file)

            if data is not None:
                vacancies = [Vacancy(item) for item in data]
                sorted_vacancy = sorted(vacancies, reverse=True)
                for i, vacancy in enumerate(sorted_vacancy):
                    print(f'{i + 1}. {vacancy}')

            else:
                print("Файл пустой")
                return data
