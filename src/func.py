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

    # Проверка длины содержимого файла JSON
    data = hh_save.read_vacancy()
    if len(data) != 0:
        query_show = input(
            "Хотите посмотреть список вакансий из существующего JSON файла(Да-'Y', Нет-'Enter')? ").title()
        if query_show == "Y":
            hh_save.show_vacancy()
        query_delete = input("Хотите для начала удалить информацию из JSON файла(Да-'Y', Нет-'Enter')? ").title()
        if query_delete != "Y":
            print("Новый запрос будет добавлен в существующий файл.")
        else:
            hh_save.del_vacancy()

    query_vacancy = input("Какую вакансию ищем? ").title()
    vacancy_city = input("В каком городе? ").title()
    query_salary = int(input("Начальный уровень зарплаты? "))
    vacancy_top_n = int(input("Сколько вакансий вывести в топе? "))

    # вызываем метод класса HeadHunterAPI для получения вакансий
    hh_vacancy = hh_api.get_vacancy(query_vacancy)
    print(repr(hh_api))

    # вызываем метод класса JSONSaver для формирования списка словарей вакансий
    list_vacancy = hh_save.get_json(hh_vacancy)

    # Сортировка по городу и добавляем в список отфильтрованные по городу вакансии.
    # создание списка ТОП вакансий, заданных пользователем
    for vacancy in list_vacancy:
        if vacancy['vacancy_city'] == vacancy_city and vacancy['salary_from'] >= query_salary:
            sorted_vacancy_list.append(vacancy)
    for vacancy in sorted_vacancy_list[:vacancy_top_n]:
        filtered_vacancy_list.append(vacancy)

    # Создаем экземпляры класса Vacancy на основе созданного списка
    vacancies = [Vacancy(item) for item in filtered_vacancy_list]

    # Сортируем в магическом методе __lt__ класса Vacancy по начальной зарплате
    sorted_vacancy = sorted(vacancies, reverse=True)

    # Выводим информацию на экран
    for i, vacancy in enumerate(sorted_vacancy[:vacancy_top_n]):
        print(f'{i + 1}. {vacancy}')

    # Считываем информацию из файла JSON
    vacancy_from_json = hh_save.read_vacancy()

    if len(vacancy_from_json) == 0:
        print("Файл был пустой")
        # Записываем отфильтрованную информаию о вакансиях в файл
        hh_save.save_vacancy(filtered_vacancy_list)
        print(
            f'По запросу найдено {len(sorted_vacancy_list)} вакансий. В файл записано {len(sorted_vacancy)} вакансий.')
        print("Информация записана в файл Vacancy_HH.json")
    else:
        # Добавляем отфильтрованную информаию о вакансиях в существующий список файла
        vacancy_from_json.extend(filtered_vacancy_list)
        # Перезаписываем файл JSON
        hh_save.save_vacancy(vacancy_from_json)
        print(
            f'По запросу найдено {len(sorted_vacancy_list)} вакансий. В файл добавлено {len(sorted_vacancy)} вакансии.')
        print("Информация добавлена в файл Vacancy_HH.json")
