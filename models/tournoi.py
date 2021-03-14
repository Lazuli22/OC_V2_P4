import re
import datetime
from constantes import REGEX
from typing import Union
from joueur import Joueur
from match import Match
from tournee import Tournee
from enum import Enum
import uuid
from seriable import Serializable



class Tournoi(Serializable):
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

    Regle_Temps = Enum('RTemps', 'Bullet Blitz Coup_rapide')

    def __init__(
            self,
            nom,
            lieu,
            date,
            list_joueurs,
            regle_temps,
            description
            ):
        """ Contructeur pour instancier un tournoi """
        self.nom = nom  # nommer un tournoi
        self.lieu = lieu  # lieu du tournoi
        self.date = date  # date du tournoi
        self.__nbre_tours = 4  # 4 tournées
        self.__tournees = []
        self.joueurs = list_joueurs
        self.regle_temps = regle_temps
        self.description = description
        date = str(self.date)
        self.identifiant = f"{self.nom}_{self.lieu}_{date}"

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        if re.search(REGEX, value):
            self.__nom = value
        else:
            print("Attention le nom du Tournoi comprend autre chose que des lettres !")

    @property
    def lieu(self) -> str:
        return self.__lieu

    @lieu.setter
    def lieu(self, value: str):
        if re.search(REGEX, value):
            self.__lieu = value
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
    def tournee(self) -> list[Tournee]:
        return self.__tournees

    @tournee.setter
    def tournees(self, tournees: list[Tournee]):
        if tournees is not None:
            self.__tournees = tournees

    @property
    def joueurs(self) -> list[uuid.UUID]:
        return self.__joueurs

    @joueurs.setter
    def joueurs(self, new_joueurs: list[uuid.UUID]):
        if new_joueurs is not None:
            self.__joueurs = new_joueurs

    @property
    def regle_temps(self):
        return self.__regle_temps

    @regle_temps.setter
    def regle_temps(self, value: Union[Regle_Temps, str]):
        if isinstance(value, str):
            try:
                self.__regle_temps = Tournoi.Regle_Temps[value]
            except KeyError:
                raise AttributeError("Impossible de déterminer la règle de temps")
        if isinstance(value, Tournoi.Regle_Temps):
            try:
                self.__regle_temps = value
            except KeyError:
                raise AttributeError(
                    "La valeur doit être de ici type Tournoi.Regle_Temps ou str"
                )

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if description is not None:
            self.__description = description

    def generer_premier_tournee(self):
        liste_matchs = Match.generer_matchs_premier_tour(Joueur.lecture_joueurs_json())
        self.tournee.append(Tournee("round1", liste_matchs))

    def serialize(self):
        """ Fonction permettant de sérialiser un Tournoi.
            Elle renvoit un dictionnaire de clefs/valeurs sur l'ensemble des 
            informations du tournoi
        """
        liste_tournee = []
        for elt in self.tournee:
            liste_tournee.append(elt.serialize())
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date": self.date,
            "nbre_tours": 4,
            "tournees": liste_tournee,
            "list_joueurs": self.joueurs,
            "regle_temps": self.regle_temps,
            "description": self.description,
            "identifiant": self.identifiant
        }


def main():
    liste_joueurs = Joueur.liste_identifiants_joueurs(Joueur.lecture_joueurs_json())
    tournoi_data = {'nom': 'Tournoi du Monde',
                    'lieu': 'Paris',
                    'date': '2021-03-13',
                    'list_joueurs': liste_joueurs,
                    'regle_temps': Tournoi.Regle_Temps.Blitz,
                    'description': 'Tournoi de renomée mondiale qui permet qui fait affonter les meilleurs joueurs mondiaux'
                    }
    un_tournoi = Tournoi(**tournoi_data)
    un_tournoi.generer_premier_tournee()
    print(un_tournoi.serialize())

if __name__ == "__main__":
    main()
