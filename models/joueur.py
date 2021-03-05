import datetime
import re
from enum import Enum
from typing import Union
from seriable import Serializable
from constantes import Const


class Joueur(Serializable):
    """ Classe qui définit un joueur d'échec caractérisé par :
    - nom
    - prénom
    - sa date de naissance
    - son sexe
    - son classement
    """

    Sexe = Enum('Sexe', 'Male Female Transgender Hermaphrodite')

    def __init__(self, nom, prenom, date_nais, jsexe, classement=0):
        """ Contructeur pour instanciation d'un joueur"""
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_nais
        self.sexe = jsexe
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
            self.__sexe = value
        else:
            raise AttributeError("La valeur doit être de type Joueur.Sexe ou  str")

    @property
    def classement(self) -> int:
        return self.__classement

    @classement.setter
    def classement(self, value: int):
        if int(value) <= 0:
            raise AttributeError("Erreur, le classement fourni ne peut être négatif")
        self.__classement = value

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
        data_dict = {}
        data_dict["nom"] = self.nom
        data_dict["prenom"] = self.prenom
        data_dict["date_naissance"] = self.date_naissance.isoformat
        data_dict["sexe"] = self.sexe.value
        data_dict["classement"] = self.classement
        print(data_dict)
        return data_dict


def main():
    dolores = Joueur("Diaz", "Dolores", "1978-08-22", "Female", 100)
    print(dolores)
   # dolores.sexe = Sexe(2)
   # ser = dolores.serialize()
   # dolores.deseralize(ser)

if __name__ == "__main__":
    main()

