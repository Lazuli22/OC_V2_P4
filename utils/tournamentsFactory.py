from utils.factory import Factory
from models.tournament import Tournament
from models.player import Player


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
    def tournaments_registry(self, list_registry: list[Player]):
        if list_registry is not []:
            self.__tournaments_registry = list_registry

    def create(self, dict_data):
        """ Create a tournaments registry """
        self.tournaments_registry.append(Tournament(**dict_data))

    def get_one_tournement(self, id_tournament):
        """ function that gets a tournament with its id"""
        for elt in self.tournaments_registry:
            ident = str(elt.identifier)
            if id_tournament == ident:
                return elt

    def addTournament(self, one_tournament):
        """ function that permits to add a Tournament without duplicate"""
        for elt in self.tournaments_registry:
            identifier = str(elt.identifier)
            if one_tournament.identifier == identifier:
                raise Exception("Vous essayez d'ajouter un tournoi existant")
            else:
                if one_tournament.name == elt.name:
                    print("Vous essayez d'ajouter un tournoi existant !")
                    raise Exception(f"Voici son idenfiant {elt.identifier}")
        self.tournaments_registry.append(one_tournament)
        print("Tournoi ajouté au sein du registre des tournois !")

