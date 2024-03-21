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
        # super().__init__()

    # def __init__(self, vacancy_title, vacancy_link, vacancy_city, company_name,
    #              salary_from, salary_to, currency, vacancy_responsibility, vacancy_requirements):
    #     self.vacancy_title = vacancy_title
    #     self.vacancy_link = vacancy_link
    #     self.vacancy_city = vacancy_city
    #     self.company_name = company_name
    #     self.salary_from = salary_from
    #     self.salary_to = salary_to
    #     self.currency = currency
    #     self.vacancy_responsibility = vacancy_responsibility
    #     self.vacancy_requirements = vacancy_requirements

    def __str__(self):
        """Добавляем строковое отображение"""
        print('*' * 150)

        return (f'Название вакансии, ссылка: {self.vacancy_title}, {self.vacancy_link}\n'
                f'Город, компания: {self.vacancy_city}, {self.company_name} \n'
                f'Уровень ЗП, валюта: {self.salary_from} - {self.salary_to}, {self.currency}\n'
                f'Описание: {self.vacancy_responsibility}\n'
                f'Требования: {self.vacancy_requirements}')

    def validate_vacancy(self):
        pass

    def check_salary_from(self):
        """Метод проверяет указан ли начальный уровень зарплаты"""
        if isinstance(self.salary_from, int) and self.salary_from > 0:
            return True
        else:
            return False

    def check_currency(self):
        """Проверка валюты RUR или USD"""
        if self.currency == "RUR":
            return 'rur'
        elif self.currency == "USD":
            return 'usd'
        else:
            return False

    def __lt__(self, other):
        return self.salary_from < other.salary_from
