from abc import ABC, abstractmethod


class Saver(ABC):
    """Создаем абстрактный класса рабты с вакансиями"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass

class JSON(Saver):

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def get_vacancy(self):
        pass

    def add_vacancy(self):
        pass

    def del_vacancy(self):
        pass