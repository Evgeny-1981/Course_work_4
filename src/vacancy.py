class Vacancy:
    vacancy_title: str  # название вакансии
    vacancy_link: str  # ссылка на вакансию
    vacancy_city: str  # город вакансии
    company_name: str  # название работодателя
    salary_from: int  # зарплата от
    salary_to: int  # зарплата до
    currency: str  # валюта
    vacancy_responsibility: str  # описание вакансии
    vacancy_requirements: str  # требования к вакансии

    def __init__(self, dictionary):
        self.vacancy_title = dictionary.get('vacancy_title')
        self.vacancy_link = dictionary.get('vacancy_link')
        self.vacancy_city = dictionary.get('vacancy_city')
        self.company_name = dictionary.get('company_name')
        self.salary_from = dictionary.get('salary_from')
        self.salary_to = dictionary.get('salary_to')
        self.currency = dictionary.get('currency')
        if dictionary.get('vacancy_responsibility'):
            self.vacancy_responsibility = dictionary.get('vacancy_responsibility')
        else:
            self.vacancy_responsibility = "Не указано"
        if dictionary.get('vacancy_requirements'):
            self.vacancy_requirements = dictionary.get('vacancy_requirements')
        else:
            self.vacancy_requirements = "Не указано"

    def __repr__(self):
        return (f'Вакансия {self.vacancy_title}, {self.vacancy_link}'
                f'{self.vacancy_city}, {self.company_name}'
                f'{self.salary_from} - {self.salary_to}, {self.currency}'
                f'{self.vacancy_responsibility}, {self.vacancy_requirements}')

    def __str__(self):
        """Добавляем строковое отображение"""
        print('*' * 150)
        return (f'Название вакансии, ссылка: {self.vacancy_title}, {self.vacancy_link}\n'
                f'Город, компания: {self.vacancy_city}, {self.company_name} \n'
                f'Уровень ЗП, валюта: {self.salary_from} - {self.salary_to}, {self.currency}\n'
                f'Описание: {self.vacancy_responsibility.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                f'Требования: {self.vacancy_requirements.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n')

    def check_salary_from(self):
        """Метод проверяет указан ли начальный уровень зарплаты"""
        if isinstance(self.salary_from, int) and self.salary_from > 0:
            return True
        else:
            return False

    def check_currency(self):
        """Проверка валюты RUR или USD, другая"""
        if self.currency == "RUR":
            return 'RUR'
        elif self.currency == "USD":
            return 'USD'
        else:
            return False

    def __lt__(self, other):
        """Метод сравнивает начальную зарплату между экземплярами класса для сортировки по возрастанию"""
        if self.salary_from is str:
            self.salary_from = 0
        if other.salary_from is str:
            other.salary_from = 0
        return self.salary_from < other.salary_from
