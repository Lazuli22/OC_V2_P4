from datetime import datetime
import re
from constantes import REGEX
from joueur import Joueur
from match import Match
from seriable import Serializable


class Tournee(Serializable):
    """
    Classe qui définit un Tour ou un round composé de
        - un nom
        - une liste de matchs
        - une date de début
        - une heure de début
        - une date de fin
        - une heure de fin
    """

    def __init__(self, nom, list_matchs):
        """ Contructeur pour instancier une tournée """
        self.nom = nom
        self.liste_matchs = list_matchs
        self.__date_debut = datetime.now()
        self.__heure_debut = 0
        self.date_fin = None
        self.heure_fin = None

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        if re.search(REGEX, value):
            self.__nom = value
        else:
            raise AttributeError(
                "Attention le nom comprend autre chose que des lettres !"
            )

    @property
    def liste_matchs(self) -> list:
        return self.__liste_matchs

    @liste_matchs.setter
    def liste_matchs(self, liste_matchs: list):
        if liste_matchs is not None:
            self.__liste_matchs = liste_matchs

    @property
    def date_debut(self) -> datetime:
        return self.__date_debut


    @property
    def heure_debut(self) -> datetime:
        return self.__heure_debut

    @property
    def date_fin(self) -> datetime:
        return self.__date_fin

    @date_fin.setter
    def date_fin(self, date_fin: datetime):
        self.__date_fin = date_fin

    @property
    def heure_fin(self) -> datetime:
        return self.__heure_fin

    @heure_fin.setter
    def heure_fin(self, heure_fin):
        self.__heure_fin = heure_fin

    def generer_premier_tournee(joueurs_json):
        """
        Fonction qui permet de générér le premier tour des matchs.
        Elle renvoit une instance de Tournée
        """
        liste_joueurs = Joueur.lecture_joueurs_json(joueurs_json)
        liste_matchs = Match.generer_matchs_premier_tour(liste_joueurs)
        return Tournee("Round 1", liste_matchs)

    def serialize(self) -> dict[str, str]:
        """ fonction qui permet de sérialiser un tour ou un round
        et retourne un dictionnaire contenant les valeurs d'un round
        """
        liste_matchs = []
        for elt in self.liste_matchs:
            liste_matchs.append(elt.serialize())        
        return {
            "nom": self.nom,
            "liste_matchs": liste_matchs,
            "date_debut": self.date_debut,
            "heure_debut": self.heure_debut,
            "date_fin": self.date_fin,
            "heure_fin": self.heure_fin
        }


def main():
    liste_matchs = Match.generer_matchs_premier_tour(Joueur.lecture_joueurs_json())
    round_un_data = Tournee("round1", liste_matchs)
    round_un_serialise = round_un_data.serialize()
    print(round_un_serialise)


if __name__ == "__main__":
    main()



















