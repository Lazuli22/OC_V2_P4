import abc
from utils.singleton import Singleton


class Controller(Singleton, metaclass=abc.ABCMeta):
    """ class to defines Controller of Chess Tournament"""

    @abc.abstractclassmethod
    def create_one(self):
        pass

    @abc.abstractclassmethod
    def get_one(self, id_element):
        pass

    @abc.abstractclassmethod
    def load_create(self, choice, id_element):
        pass

    