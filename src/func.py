import encodings
from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    query_vacancy = input("Какую вакансию ищем? ")
    # other_params = input("Желаете уточнить параметры поиска? (Да(Y)/Нет(N)")
    # if other_params.lower() == "Y":
    # query_city = input("В каком городе? ")
    # query_salary = input("Начальный уровень зарплаты? ")
    # query_n_vacancy = input("Сколько вакансий вывести? ")
    currency = input('В какой валюте интересуют вакансии? ')

    hh_api = HeadHunterAPI()
    hh_vacancy = hh_api.get_vacancy(query_vacancy)

    print(repr(hh_api))
    list_json_vacancy = hh_api.save_json(hh_vacancy)
    # print(list_json_vacancy)
    instances = [Vacancy(item) for item in list_json_vacancy] #Создание экземпляров класса Вакансии из списка
    for instance in instances:
        if instance.check_currency() == 'rur':
            print(instance)
    #

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

    # for item in hh_vacancy:
    #     if isinstance(item['salary_from'], int):
    # sorted_vacancy = sorted(hh_vacancy, key=lambda x: x['salary_from'], reverse=True)
    #
    # for item in sorted_vacancy[:5]:
    #     print(item)

