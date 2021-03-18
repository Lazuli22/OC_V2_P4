import abc
from models.tournament import Tournament
from models.player import Player


class Factory(metaclass=abc.ABCMeta):
    """
    abstract class that creates element of a tounament
    """

    @abc.abstractclassmethod
    def create(self, dict_data):
        """
        abstract method that creates a tournament or a player
        with a dict of data.
        """
        pass


class Factory_tournament(Factory):

    def create(self, dict_data):
        """ Create a tournament """
        return Tournament(**dict_data)


class Factory_player(Factory):

    def create(self, dict_data):
        """ Create a player """
        return Player(**dict_data)