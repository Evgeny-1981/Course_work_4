import encodings
from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    query_vacancy = input("Какую вакансию ищем? ")
    user_top_n = int(input("Сколько вакансий вывести в топе? "))
    query_city = input("В каком городе? ")
    # other_params = input("Желаете уточнить параметры поиска? (Да(Y)/Нет(N)")
    # if other_params.lower() == "Y":
    # query_salary = input("Начальный уровень зарплаты? ")
    # query_n_vacancy = input("Сколько вакансий вывести? ")
    # currency = input('В какой валюте интересуют вакансии? ')

    hh_api = HeadHunterAPI()
    hh_vacancy = hh_api.get_vacancy(query_vacancy)

    print(repr(hh_api))
    list_json_vacancy = hh_api.save_json(hh_vacancy)

    vacancies = [Vacancy(item) for item in list_json_vacancy]  # Создание экземпляров класса Вакансии из списка
    sorted_vacancy_list = []
    for vacancy in vacancies:
        if isinstance(vacancy.salary_from, int):
            sorted_vacancy = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)

    sorted_vacancy_list = sorted_vacancy
    # print(sorted_vacancy_list)
    # for item in sorted_vacancy_list:
    #
    for vacancy in sorted_vacancy_list:
    for vacancy in vacancies[0:user_top_n]:
        if vacancy.vacancy_city == query_city:
            # print(f'{n}.{vacancy}')

    # key_list = ["vacancy_title", "vacancy_link", "vacancy_city", "company_name", "salary_from",
    #             "salary_to", "currency", "vacancy_responsibility", "vacancy_requirements"]
    # vacancy_title = input("Введите название вакансии: ")
    # vacancy_link = input("Укажите ссылку на вакансию: ")
    # vacancy_city = input("Укажите город: ")
    # company_name = input("Укажите название компании: ")
    # salary_from = input("Уажите зарплату ОТ: ")
    # salary_to = input("Укажите ззарплату ДО: ")
    # currency = input("Валюта зарплаты: ")
    # vacancy_responsibility = input("Краткое описание вакансии: ")
    # vacancy_requirements = input("Требования к соискателю: ")
    # value_list = [vacancy_title, vacancy_link, vacancy_city, company_name, salary_from, salary_to,
    #              currency, vacancy_responsibility, vacancy_requirements]
    # dict_new_vacancy = dict(zip(key_list, value_list*len(key_list)))
    #
    # vac1 = Vacancy(dict_new_vacancy)

    # hh_vacancy = hh_api.get_vacancy(query_vacancy)
    # print(hh_vacancy)

    # if isinstance(item['salary_from'], int):
    # sorted_vacancy = sorted(list_json_vacancy, key=lambda x: x['salary_from'], reverse=True)
    # #
    # for item1 in sorted_vacancy[:5]:
    #     print(item1)
