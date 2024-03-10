import json
import requests
import time
import os
from src.Abstract_classes import AbstractAPI


class HeadHunterAPI:
    url = 'https://api.hh.ru/vacancies'

    def get_vacancy(self, name):
        list_vacancy = []
        params = {
            'text': f'NAME:{name}',  # Текст фильтра. В имени должно быть слово "Аналитик"
            # 'area': 2,  # Поиск ощуществляется по вакансиям города Москва
            'page': 10,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        return data

p = HeadHunterAPI()
print(p.get_vacancy('Менеджер'))
