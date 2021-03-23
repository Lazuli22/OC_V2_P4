from models.factory import Factory
from models.tournament import Tournament


class TournamentsFactory(Factory):

    __instance = None

    @staticmethod
    def getInstance():
        if TournamentsFactory.__instance is None:
            TournamentsFactory()
        return TournamentsFactory.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if TournamentsFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TournamentsFactory.__instance = self
            self.__tournaments_registry = []

    @property
    def tournaments_registry(self) -> list:
        return self.__tournaments_registry

    @tournaments_registry.setter
    def tournaments_registry(self, list_registry):
        if list_registry is not []:
            self.__tournaments_registry = list_registry

    def create(self, dict_data):
        """ Create a tournaments registry """
        self.tournaments_registry.append(Tournament(**dict_data))
