import json
import requests
import time
import os

from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Создаем абстрактный класс для класса APIconnect"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass



class HeadHunterAPI:
    url = 'https://api.hh.ru/vacancies'

    def get_vacancy(self, name):
        list_vacancy = []
        params = {
            'text': f'NAME:{name}',  # Текст фильтра. В имени должно быть слово "Аналитик"
            'page': 1,  # Индекс страницы поиска на HH
            'per_page': 1  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params=params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()

        return data



p = HeadHunterAPI()
print(p.get_vacancy('Python'))

