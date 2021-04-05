from utils.factory import Factory
from utils.singleton import Singleton
from models.player import Player


class PlayersFactory(Factory, Singleton):

    __instance = None

    @staticmethod
    def getInstance():
        if not PlayersFactory.__instance:
            PlayersFactory()
        return PlayersFactory.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if PlayersFactory.__instance:
            raise Exception("This class is a singleton!")
        else:
            PlayersFactory.__instance = self
            self.__players_registry = []

    @property
    def players_registry(self) -> list:
        return self.__players_registry

    @players_registry.setter
    def players_registry(self, list_registry: list):
        if list_registry:
            self.__players_registry = list_registry

    def create(self, dict_data):
        """ Create a players registry with list of players"""
        for elt in dict_data:
            self.players_registry.append(elt)

    def addPlayer(self, one_player):
        """ function that permits to add a player without duplicate"""
        for elt in self.players_registry:
            ident = str(elt.identifier)
            if one_player.identifier == ident:
                raise Exception("Vous essayez d'ajouter un joueur existant")
            else:
                if one_player.firstname == elt.firstname and one_player.lastname == elt.lastname:
                    print("Vous essayez d'ajouter un joueur existant !")
                    raise Exception(f"Voici son idenfiant {elt.identifier}")
        self.players_registry.append(one_player)
        print("joueur ajouté au sein du registre des joueurs !")
            
    def get_one_player(self, id_player: str):
        """ function that gets a player with his id """
        for elt in self.players_registry:
            ident = str(elt.identifier)
            if id_player == ident:
                return elt
            

        
