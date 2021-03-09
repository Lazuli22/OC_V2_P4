import datetime
import re
import json
from enum import Enum
from typing import Union
from seriable import Serializable
from constantes import Const
import uuid


class Joueur(Serializable):
    """ Classe qui définit un joueur d'échec caractérisé par :
    - uuid
    - nom
    - prénom
    - sa date de naissance
    - son sexe
    - son classement
    """

    Sexe = Enum('Sexe', 'Male Female Transgender Hermaphrodite')

    def __init__(self, nom, prenom, date_naissance, sexe, classement=0, identifiant=uuid.uuid4():
        """ Contructeur pour instanciation d'un joueur"""
        self.identifiant = identifiant
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement


    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        if re.search(Const.REGEX, value):
            self.__nom = value
        else:
            raise AttributeError("Attention le nom comprend autre chose que des lettres !")

    @property
    def prenom(self) -> str:
        return self.__prenom

    @prenom.setter
    def prenom(self, value: str):
        if re.search(Const.REGEX, value):
            self.__prenom = value
        else:
            raise AttributeError("Attention le prénom comprend autre chose que des lettres !")

    @property
    def date_naissance(self) -> datetime.date:
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, value: Union[str, datetime.date]):
        if isinstance(value, str):
            try:
                value = datetime.date.fromisoformat(value)
            except ValueError:
                raise AttributeError("Impossible de déterminer la date")
        age = datetime.date.today().year - value.year
        if (age < 7 or age > 77):
            raise AttributeError("Attention le joueur est agé de "+str(age)+" années \
                Il ne peut participer au tournoi")
        else:
            self.__date_naissance = value

    @property
    def sexe(self) -> Sexe:
        return self.__sexe

    @sexe.setter
    def sexe(self, value: Union[Sexe, str]):
        if isinstance(value, str):
            try:
                self.__sexe = Joueur.Sexe[value]
            except KeyError:
                raise AttributeError("Impossible de déterminer le sexe")
        if isinstance(value, Joueur.Sexe):
            try:
                self.__sexe = value
            except KeyError:
                raise AttributeError("La valeur doit être de ici type Joueur.Sexe ou str")

    @property
    def classement(self) -> int:
        return self.__classement

    @classement.setter
    def classement(self, value: int):
        if int(value) <= 0:
            raise AttributeError("Erreur, le classement fourni ne peut être négatif")
        self.__classement = value

    @property
    def identifiant(self):
        return self.__identifiant

    @identifiant.setter
    def identifiant(self, value: Union[uuid,str]):
        if isinstance(value, str):
            try:
             self.identifiant = uuid4(value)
            except  ValueError :
                raise  AttributeError ("Erreur....."
            
        if isinstance(value,uuid):
            if(value.version == 4):
                self.__identifiant = value
            else:
                raise AttributeError("Erreur...")
  


    def __repr__(self) -> str:
        """ fonction permettant de représenter un joueur"""
        return (
            f"<Joueur {self.__prenom},"
            f"{self.__nom},"
            f"(date de naissance={self.__date_naissance},"
            f"sexe={self.__sexe},"
            f"classement={self.__classement})>"
        )

    def serialize(self) -> dict[str, str]:
        """ fonction qui permet de serialiser un Joueur, en sortie
        nous obtenons un dictionnaire contenant les informations du  joueur """
        data_dict = {}
        data_dict["nom"] = self.nom
        data_dict["prenom"] = self.prenom
        data_dict["date_naissance"] = self.date_naissance.strftime("%Y-%m-%d")
        data_dict["sexe"] = self.sexe.name
        data_dict["classement"] = self.classement
        return data_dict

    def lecture_joueurs_json():
        """fonction permettant de lire un fichier json et de
         produire une liste de Joueurs
        """
        liste_joueurs = []
        with open("joueurs.json") as f:
            data = json.load(f)
        for elt in data:
            liste_joueurs.append(Joueur(
                elt["joueur"]["nom"],
                elt["joueur"]["prenom"],
                elt["joueur"]["date_naissance"],
                elt["joueur"]["sexe"],
                elt["joueur"]["classement"]
            ))
        return liste_joueurs


def main():
    #print(Joueur.lecture_joueurs_json())
    dolores_data = {'nom' : 'Diaz', 'prenom': 'Dolores', 'date_naissance':'1978-08-22', 'sexe': 'Female', 'classement': 100 }
    dolores = Joueur(**dolores_data)
    assert dolores.serialize() == dolores_data


if __name__ == "__main__":
    main()
