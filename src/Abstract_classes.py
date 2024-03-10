from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Создаем абстрактный класс для класса APIconnect"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass



class AbstractVacancy(ABC):
    """Создаем абстрактный класс для класса Vacancy"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def compare_vacancy(self):
        pass

    @abstractmethod
    def validate_data(self):
        pass