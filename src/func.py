from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    query_vacancy = input("Input vacancy name ")
    # other_params = input("������� �������� ��������� ������? (��(Y)/���(N)")
    # if other_params.lower() == "Y":
    # query_city = input("� ����� ������? ")
    # query_salary = input("��������� ������� ��������? ")
    # query_n_vacancy = input("������� �������� �������? ")

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
