import json
import os

from config import DATA_PATH


class Vacancy:
    vacancy_title: str  # название вакансии
    vacancy_link: str  # ссылка на вакансию
    vacancy_city: str  # город вакансии
    company_name: str  # название работодателя
    salary_from: float  # зарплата от
    salary_to: float  # зарплата до
    vacancy_responsibility: str  # описание вакансии
    vacancy_requirements: str  # требования к вакансии

    def __init__(self, vacancy_title, vacancy_link, vacancy_city, company_name,
                 salary_from, salary_to, vacancy_responsibility, vacancy_requirements):
        self.vacancy_title = vacancy_title
        self.vacancy_link = vacancy_link
        self.vacancy_city = vacancy_city
        self.company_name = company_name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.vacancy_responsibility = vacancy_responsibility
        self.vacancy_requirements = vacancy_requirements

    def __str__(self):
        """Добавляем строковое отображение"""
        return (f'{self.vacancy_title}, {self.vacancy_link}, {self.vacancy_city}, '
                f'{self.company_name}, {self.salary_from}-'
                f'{self.salary_to}, {self.vacancy_responsibility}, {self.vacancy_requirements}')

    def validate_vacancy(self):
        pass

    def validate_salary(self):
        """Проверка по зарплате"""
        if self.salary_from:
            return True
        elif self.salary_to:
            return True
        else:
            return False

    @staticmethod
    def __lt__(self, other):
        if self.salary_from > other.salary_from:
            return self.salary_from


