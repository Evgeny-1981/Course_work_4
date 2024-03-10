class Vacancy:
    vacancy_title: str  # название вакансии
    vacancy_link: str  # ссылка на вакансию
    vacancy_company_name: str  # название работодателя
    vacancy_address: str  # адрес работодателя
    employment_mode: str  # режим работы
    work_experience: str  # опыт работы
    salary_compensation_from: float  # зарплата от
    salary_compensation_to: float  # зарплата до
    vacancy_responsibility: str  # описание вакансии
    vacancy_requirements: str  # требования к вакансии

    def __init__(self, vacancy_title, vacancy_link, vacancy_company_name, vacancy_address,
                 employment_mode, work_experience, salary_compensation_from, salary_compensation_to,
                 vacancy_responsibility, vacancy_requirements):
        self.vacancy_title = vacancy_title
        self.vacancy_link = vacancy_link
        self.vacancy_company_name = vacancy_company_name
        self.vacancy_address = vacancy_address
        self.employment_mode = employment_mode
        self.work_experience = work_experience
        self.salary_compensation_from = salary_compensation_from
        self.salary_compensation_to = salary_compensation_to
        self.vacancy_responsibility = vacancy_responsibility
        self.vacancy_requirements = vacancy_requirements

    def __str__(self):
        """Добавляем строковое отображение"""
        return (f'{self.vacancy_title}, {self.vacancy_link}, {self.vacancy_company_name}, '
                f'{self.vacancy_address}, {self.vacancy_address}, {self.employment_mode},'
                f'{self.employment_mode}, {self.work_experience}, {self.salary_compensation_from}-'
                f'{self.salary_compensation_to}, {self.vacancy_responsibility}, {self.vacancy_requirement}')

    def compare_vacancy(self):
        pass

    def validate_data(self):
        pass
