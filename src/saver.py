import json
import os
from abc import ABC, abstractmethod
from config import DATA_PATH
from src.vacancy import Vacancy
import re


class Saver(ABC):
    """Создаем абстрактный класса работы с вакансиями"""

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
    def save_vacancy(self, vacancy_list):
        pass

    @abstractmethod
    def read_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass

    @abstractmethod
    def show_vacancy(self):
        pass


class JSONSaver(Saver):
    """Создаем класс для работы с JSON файлом"""

    def __init__(self):
        self.file_json = os.path.join(DATA_PATH, f'Vacancy_HH.json')
        self.file_name = self.file_json
        self.data_json = []
        if not os.path.exists(self.file_json):
            with open(self.file_json, 'w+') as file:
                json.dump(self.data_json, file)
                print(f"Создан файл для записи результатов по пути - {self.file_json}")
        self.vacancy_list = []

    def __repr__(self):
        return f'Создан экземпляр класса {self.__class__.__name__}\n'

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

    def save_vacancy(self, vacancy_list):
        """Метод для сохранения вакансий в JSON файл"""
        with open(self.file_json, 'w', encoding='utf-8', errors='ignore') as file:
            json.dump(vacancy_list, file, indent=4, ensure_ascii=False)
        # return json.dump(vacancy_list, file, indent=4, ensure_ascii=False)

    def read_vacancy(self):
        """Метод для чтения вакансий из JSON файла"""
        with open(self.file_json, 'r', encoding='utf-8', errors='ignore') as file:
            data = json.load(file)
        return data

    def del_vacancy(self):
        """Метод для удаления вакансий из JSON файла"""
        with open(self.file_json, 'w') as file:
            json.dump(self.data_json, file)
        print("Данные удалены")

    def show_vacancy(self):
        """Метод для отображения вакансий из сохраненного ранее JSON файла"""
        show_list = []
        with open(self.file_json, 'r', encoding='utf-8', errors='ignore') as file:
            data = json.load(file)
            if len(data) != 0:
                query_vacancy = input(
                    "Какую вакансию ищем (введите ключевое слово и нажмите Enter)? Enter - показать все: ").title()
                for item in data:
                    strings = re.split('-| |/|"', item['vacancy_title'])
                    for string in strings:
                        if query_vacancy.lower() in string.lower():
                            show_list.append(item)
                if len(show_list) == 0:
                    print("По введенному ключевому слову вакансий не найдено.")
                vacancies = [Vacancy(item) for item in show_list]
                sorted_vacancy = sorted(vacancies, reverse=True)
                for i, vacancy in enumerate(sorted_vacancy):
                    print(f'{i + 1}. {vacancy}')
            else:
                print("Файл с вакансиями пуст.")
        return data
