import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Создаем абстрактный класс для HeadHunterAPI"""

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
    """Класс для получения вакансий с сайта HeadHanter"""

    def __init__(self):
        self.url = 'http://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'search_field': 'name'}
        self.vacancy = []

    def __repr__(self):
        return f'Ожидайте, выполняется подключение класса {self.__class__.__name__} к сайту HH для получения вакансии...\n'

    def get_vacancy(self, query_vacancy):
        """Метод для запроса к HeadHunter для получения вакансий"""
        self.params['text'] = query_vacancy
        while self.params.get('page') != 10:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancy = response.json()['items']
            self.vacancy.extend(vacancy)
            self.params['page'] += 1

        return self.vacancy