import encodings
from src.api import HeadHunterAPI
from src.saver import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    query_vacancy = input("Какую вакансию ищем? ").title()
    vacancy_city = input("В каком городе? ").title()
    vacancy_top_n = int(input("Сколько вакансий вывести в топе? "))
    # query_salary = input("Начальный уровень зарплаты? ")

    hh_api = HeadHunterAPI()  # создание экземпляра класса HeadHunterAPI
    hh_vacancy = hh_api.get_vacancy(query_vacancy)  # вызываем метод класса HeadHunterAPI для получения вакансий
    print(repr(hh_api))

    hh_save = JSONSaver()  # создаем экземпляр класса JSONSaver
    list_vacancy = hh_save.get_json(hh_vacancy)  # вызываем метод класса JSONSaver для формирования саиска вакансий

    vacancies = [Vacancy(item) for item in list_vacancy]  # Создание экземпляров класса Вакансии из списка
    # print(vacancies, sep='\n')
    sorted_vacancy_list = []
    filtered_vacancy_list = []
    # sorted_vacancy = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)
    sorted_vacancy = sorted(vacancies, reverse=True)

    n = 0
    for vacancy in sorted_vacancy:
        if vacancy.vacancy_city == vacancy_city:
            sorted_vacancy_list.append(vacancy)
    for n, vacancy in enumerate(sorted_vacancy_list[:vacancy_top_n]):
        filtered_vacancy_list.append(vacancy)
        print(f'{n + 1}. {vacancy}')

    hh_save.save_vacancy(filtered_vacancy_list)


    # # for vacancy in sorted_vacancy_list:
    # #     for vacancy in vacancies[0:user_top_n]:
    # #         if vacancy.vacancy_city == query_city:
    # #         # print(f'{n}.{vacancy}')
    #
    # # key_list = ["vacancy_title", "vacancy_link", "vacancy_city", "company_name", "salary_from",
    # #             "salary_to", "currency", "vacancy_responsibility", "vacancy_requirements"]
    # # vacancy_title = input("Введите название вакансии: ")
    # # vacancy_link = input("Укажите ссылку на вакансию: ")
    # # vacancy_city = input("Укажите город: ")
    # # company_name = input("Укажите название компании: ")
    # # salary_from = input("Уажите зарплату ОТ: ")
    # # salary_to = input("Укажите ззарплату ДО: ")
    # # currency = input("Валюта зарплаты: ")
    # # vacancy_responsibility = input("Краткое описание вакансии: ")
    # # vacancy_requirements = input("Требования к соискателю: ")
    # # value_list = [vacancy_title, vacancy_link, vacancy_city, company_name, salary_from, salary_to,
    # #              currency, vacancy_responsibility, vacancy_requirements]
    # # dict_new_vacancy = dict(zip(key_list, value_list*len(key_list)))
    # #
    # # vac1 = Vacancy(dict_new_vacancy)
    #
    # # hh_vacancy = hh_api.get_vacancy(query_vacancy)
    # # print(hh_vacancy)
    #
    # # if isinstance(item['salary_from'], int):
    # # sorted_vacancy = sorted(list_json_vacancy, key=lambda x: x['salary_from'], reverse=True)
    # # #
