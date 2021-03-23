from models.factory import Factory
from models.player import Player


class PlayersFactory(Factory):

    __instance = None

    @staticmethod
    def getInstance():
        """ Return the singleton instance of Playersregistry """
        if PlayersFactory.__instance is None:
            PlayersFactory()
        return PlayersFactory.__instance

    def __init__(self):
        """ create the PlayersFactory Singleton with
            a players registry (empty list)
         """
        if PlayersFactory.__instance is not None:
            raise Exception("This class is a singlon")
        else:
            PlayersFactory.__instance = self
            self.__players_registry = []

    @property
    def players_registry(self) -> list:
        return self.__players_registry

    @players_registry.setter
    def players_registry(self, list_registry: list):
        if list_registry is not []:
            self.__players_registry = list_registry

    def create(self, dict_data):
        """ Create a players registry with list of players"""
        for elt in dict_data:
            self.players_registry.append(elt)
        
