from abc import ABC, abstractmethod


class SaverJSON(ABC):
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