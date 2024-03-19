from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    query_vacancy = input("Input vacancy name ")
    # other_params = input("Желаете уточнить параметры поиска? (Да(Y)/Нет(N)")
    # if other_params.lower() == "Y":
    # query_city = input("В каком городе? ")
    # query_salary = input("Начальный уровень зарплаты? ")
    # query_n_vacancy = input("Сколько вакансий вывести? ")

    hh_api = HeadHunterAPI()
    hh_vacancy = hh_api.get_vacancy(query_vacancy)
    print(repr(hh_api))
    list_json_vacancy = hh_api.save_json(hh_vacancy)


    # print(hh_vacancy)

    # hh_vacancy = hh_api.get_vacancy(query_vacancy)

    # for item in hh_vacancy:
    #     if isinstance(item['salary_from'], int):
    # sorted_vacancy = sorted(hh_vacancy, key=lambda x: x['salary_from'], reverse=True)
    #
    # for item in sorted_vacancy[:5]:
    #     print(item)
