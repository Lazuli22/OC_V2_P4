import datetime
import re
import json
import uuid
from enum import Enum
from typing import Union
from seriable import Serializable
from constantes import REGEX


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

    def __init__(
        self,
        nom,
        prenom,
        date_naissance,
        sexe,
        classement=0
        ):
        """ Contructeur pour instanciation d'un joueur"""
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.identifiant = uuid.uuid4()


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
    def prenom(self) -> str:
        return self.__prenom

    @prenom.setter
    def prenom(self, value: str):
        if re.search(REGEX, value):
            self.__prenom = value
        else:
            raise AttributeError(
                "Attention le prénom comprend autre chose que des lettres !"
                )

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
                raise AttributeError(
                    "La valeur doit être de ici type Joueur.Sexe ou str"
                )

    @property
    def classement(self) -> int:
        return self.__classement

    @classement.setter
    def classement(self, value: int):
        if int(value) < 0:
            raise AttributeError(
        "Erreur, le classement fourni ne peut être négatif"
        )
        self.__classement = value

    @property
    def identifiant(self) -> str:
        return self.__identifiant

    @identifiant.setter
    def identifiant(self, value: Union[uuid.UUID, str]):
        if isinstance(value, str):
            try:
                self.__identifiant = uuid.uuid4(value)
            except ValueError:
                raise AttributeError(
                    "Erreur sur la génération de l'identifiant")
        if isinstance(value, uuid.UUID):
            if(value.version == 4):
                self.__identifiant = str(value)
        else:
            raise AttributeError("Erreur...")

    def __repr__(self) -> str:
        """ fonction permettant de représenter un joueur"""
        return (
            f"<Joueur {self.__prenom},"
            f"{self.__nom},"
            f"(date de naissance={self.__date_naissance},"
            f"sexe={self.__sexe},"
            f"classement={self.__classement},"
            f"identifiant={self.__identifiant})>"
        )

    def serialize(self):
        """ fonction qui permet de serialiser un Joueur, en sortie
        nous obtenons un dictionnaire contenant les informations du  joueur """
        return {
                "nom": self.nom,
                "prenom": self.prenom,
                "date_naissance": self.date_naissance.strftime("%Y-%m-%d"),
                "sexe": self.sexe.name,
                "classement": self.classement,
                "identifiant": self.identifiant
            }
 
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

    def liste_identifiants_joueurs(liste_joueurs):
        list_id_joueurs = []
        for elt in liste_joueurs:
            list_id_joueurs.append(elt.identifiant)
        return list_id_joueurs


def main():
    liste_joueurs = Joueur.lecture_joueurs_json()
    print(Joueur.liste_identifiants_joueurs(liste_joueurs))
    #dolores_data = {'nom': 'Diaz', 'prenom': 'Dolores', 'date_naissance': '1978-08-22', 'sexe': 'Female', 'classement': 100}
    #dolores = Joueur(**dolores_data).serialize()
    #print(dolores)


if __name__ == "__main__":
    main()
