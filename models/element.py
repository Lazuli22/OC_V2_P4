import abc
from tournoi import Tournoi
from joueur import Joueur


class Element(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def creer_element(self, dict_data):
        pass


class Element_tournoi(Element):

    def creer_element(self, dict_data):
        un_tournoi = Tournoi(**dict_data)
        un_tournoi.generer_premier_tournee()
        return un_tournoi


class Element_joueur(Element):

    def creer_element(self, dict_data):
        return Joueur(**dict_data)