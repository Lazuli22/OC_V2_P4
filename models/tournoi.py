import re
import datetime
from constantes import Const
from typing import Union
from joueur import Joueur
from match import Match
from operator import attrgetter


class Tournoi:
    """ Classe définissant un tournoi caractérisé par
    - nom
    - Lieu
    - Date
    - Nombre de tours
    - Tournees
    - Liste de joueurs
    - Contrôle du temps
    - Description
    """

    def ___init__(self, nomT, lieuT, list_joueurs, dateT, des):
        """ Contructeur pour instancier un tournoi """
        self.nom = nomT  # nommer un tournoi
        self.lieu = lieuT  # lieu du tournoi
        self.date = dateT  # date du tournoi
        self.__nbre_tours = 4
        self.__tournées = []
        self.joueurs = list_joueurs
        self.__regle_temps = 0
        self.description = des

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        if re.search(Const.REGEX, value):
            self.__nom = value
        else:
            print("Attention le nom du Tournoi comprend autre chose que des lettres !")

    @property
    def lieu(self) -> str:
        return self.__lieu

    @lieu.setter
    def lieu(self, value: str):
        if re.search(Const.REGEX, value):
            self.__nom = value
        else:
            print("Attention le nom du Tournoi comprend autre chose que des lettres !")

    @ property
    def date(self) -> datetime.date:
        return self.__date

    @date.setter
    def date(self, dateT: Union[str, datetime.date]):
        try:
            if isinstance(dateT, str):
                dateT = datetime.date.fromisoformat(dateT)
                self.__date = dateT
        except ValueError:
            raise AttributeError("Impossible de déterminer la date")
        try:
            if isinstance(dateT, datetime.date):
                self.__date = dateT
        except ValueError:
            raise AttributeError("Impossible de déterminer la date")


    @property
    def tournees(self) -> list[str]:
        return self.__tournees

    @tournees.setter
    def tournees(self, tourneesT):
        if tourneesT is not None:
            self.__tournees = tourneesT

    @property
    def joueurs(self) -> list[Joueur]:
        return self.__joueurs

    @joueurs.setter
    def joueurs(self, new_joueurs):
        if new_joueurs is not None:
            self.__joueurs = new_joueurs
    
    @property
    def temps(self):
        return self.__temps

    @temps.setter
    def temps(self, tempsT):
        if tempsT is not None:
            self.__temps = tempsT

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, des):
        if des is not None:
            self.__description = des

    def generer_premier_tour(list_joueur):
        """ fonction permettant de générer les matchs du 1er Tour,
            retournant une liste de match
        """
        list_matchs = []
        list_triee = sorted(
                        list_joueur,
                        key=attrgetter("classement"),
                        reverse=True
                        )
        list_matchs.append(Match("Match1", list_triee[0], 0, list_triee[4], 0))
        list_matchs.append(Match("Match2", list_triee[1], 0, list_triee[5], 0))
        list_matchs.append(Match("Match3", list_triee[2], 0, list_triee[6], 0))
        list_matchs.append(Match("Match4", list_triee[3], 0, list_triee[7], 0))
        return list_matchs
        

def main():
    list_joueur = Joueur.lecture_joueurs_json()
    print(Tournoi.generer_premier_tour(list_joueur))


if __name__ == "__main__":
    main()
