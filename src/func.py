from src.api import HeadHunterAPI
from src.saver import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    sorted_vacancy_list = []
    filtered_vacancy_list = []

    # создание экземпляра класса HeadHunterAPI
    hh_api = HeadHunterAPI()

    # создаем экземпляр класса JSONSaver
    hh_save = JSONSaver()
    data = hh_save.read_vacancy()
    # vacancy_show = Vacancy(hh_save.read_vacancy())
    # if hh_save.show_vacancy() is not None:
    if data is not None:
        query_show = input(
            "Хотите посмотреть список вакансий из существующего JSON файла(Да - Y, Нет - Enter)? ").title()
        if query_show == "Y":
            hh_save.show_vacancy()

    # if hh_save.show_vacancy is not None:
    if data is not None:
        query_delete = input("Хотите для начала удалить информацию из JSON файла(Да - Y, Нет - Enter)? ").title()
        if query_delete == "Y":
            hh_save.del_vacancy()
        else:
            print("Новый запрос будет добавлен в существующий файл")

    query_vacancy = input("Какую вакансию ищем? ").title()
    vacancy_city = input("В каком городе? ").title()
    query_salary = int(input("Начальный уровень зарплаты? "))
    vacancy_top_n = int(input("Сколько вакансий вывести в топе? "))

    # вызываем метод класса HeadHunterAPI для получения вакансий
    hh_vacancy = hh_api.get_vacancy(query_vacancy)
    print(repr(hh_api))

    # вызываем метод класса JSONSaver для формирования списка словарей вакансий
    list_vacancy = hh_save.get_json(hh_vacancy)

    # сортировка по городу и добавляем в список отфильтрованные по городу вакансии.
    # создание списка ТОП вакансий, заданных пользователем
    for vacancy in list_vacancy:
        if vacancy['vacancy_city'] == vacancy_city and vacancy['salary_from'] >= query_salary:
            sorted_vacancy_list.append(vacancy)
    for vacancy in sorted_vacancy_list[:vacancy_top_n]:
        filtered_vacancy_list.append(vacancy)

    # Сохраняем список отфильрованных вакансий в JSON
    save_vacancy_list = hh_save.save_vacancy(filtered_vacancy_list)

    # Создаем экземпляры класса Vacancy на основе созданного списка
    vacancies = [Vacancy(item) for item in save_vacancy_list]

    # Сортируем в магическом методе __lt__ класса Vacancy по начальной зарплате
    sorted_vacancy = sorted(vacancies, reverse=True)

    # Выводим информацию на экран
    for i, vacancy in enumerate(sorted_vacancy[:vacancy_top_n]):
        print(f'{i + 1}. {vacancy}')

    key_list = ["vacancy_title", "vacancy_link", "vacancy_city", "company_name", "salary_from",
                "salary_to", "currency", "vacancy_responsibility", "vacancy_requirements"]
    vacancy_title = input("Введите название вакансии: ")
    vacancy_link = input("Укажите ссылку на вакансию: ")
    vacancy_city = input("Укажите город: ")
    company_name = input("Укажите название компании: ")
    salary_from = int(input("Уажите зарплату ОТ: "))
    salary_to = int(input("Укажите ззарплату ДО: "))
    currency = input("Валюта зарплаты: ")
    vacancy_responsibility = input("Краткое описание вакансии: ")
    vacancy_requirements = input("Требования к соискателю: ")
    value_list = [vacancy_title, vacancy_link, vacancy_city, company_name, salary_from, salary_to,
                  currency, vacancy_responsibility, vacancy_requirements]
    dict_new_vacancy = dict(zip(key_list, value_list * len(key_list)))

    # Считываем информацию из файла JSON
    filtered_vacancy_list = hh_save.read_vacancy()

    # Добавляем новый словарь с вакансиями
    filtered_vacancy_list.append(dict_new_vacancy)

    # Перезаписываем файл JSON
    hh_save.save_vacancy(filtered_vacancy_list)

    # # if isinstance(item['salary_from'], int):
    # # sorted_vacancy = sorted(list_json_vacancy, key=lambda x: x['salary_from'], reverse=True)
