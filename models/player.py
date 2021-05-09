import datetime
import re
import uuid
from enum import Enum
from typing import Union
from models.seriable import Serializable
from models.constants import REGEX


class Player(Serializable):
    """ Class defines a player who is characteriszed :
    - uuid
    - firstname
    - lastname
    - day of birth
    - sexe
    - rank
    - identifier
    """

    Sexe = Enum('Sexe', 'Male Female Transgender Hermaphrodite')

    def __init__(
            self,
            firstname,
            lastname,
            date_of_birth,
            sexe,
            rank,
            identifier=None
            ):
        errors = []
        try:
            self.firstname = firstname
        except AttributeError as e:
            errors.append(f"firstname: {str(e)}")
        try:
            self.lastname = lastname
        except AttributeError as e:
            errors.append(f"lastname: {str(e)}")
        try:
            self.date_of_birth = date_of_birth
        except AttributeError as e:
            errors.append(f"date de naissance: {str(e)}")
        try:
            self.sexe = sexe
        except AttributeError as e:
            errors.append(f"sexe: {str(e)}")
        try:
            self.rank = rank
        except AttributeError as e:
            errors.append(f"classement: {str(e)}")
        try:
            self.identifier = identifier if identifier else uuid.uuid4()
        except AttributeError as e:
            errors.append(f"idenfiant: {str(e)}")
        if errors:
            raise Exception(errors)

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, value: str):
        if re.search(REGEX, value):
            self.__firstname = value
        else:
            raise AttributeError(
                "Attention the firstname includes other things than letters !"
                )

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str):
        if re.search(REGEX, value):
            self.__lastname = value
        else:
            raise AttributeError(
                "Attention  the lastname includes other things than letters !"
                )

    @property
    def date_of_birth(self) -> datetime.date:
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: Union[str, datetime.date]):
        if isinstance(value, str):
            try:
                value = datetime.date.fromisoformat(value)
            except ValueError:
                raise AttributeError("impossible to determine the date")
        age = datetime.date.today().year - value.year
        if (age < 7 or age > 77):
            raise AttributeError("Attention the player is "+str(age)+" years old \
                He or she can't particite to the competition")
        else:
            self.__date_of_birth = value

    @property
    def sexe(self) -> Sexe:
        return self.__sexe

    @sexe.setter
    def sexe(self, value: Union[Sexe, str]):
        if isinstance(value, str):
            try:
                self.__sexe = Player.Sexe[value]
            except KeyError:
                raise AttributeError("Impossible to determine the sexe")
        if isinstance(value, Player.Sexe):
            try:
                self.__sexe = value
            except KeyError:
                raise AttributeError(
                    "the type must be Joueur.Sexe or str"
                )

    @property
    def rank(self) -> float:
        return self.__rank

    @rank.setter
    def rank(self, value: float):
        if float(value) < 0:
            raise AttributeError(
                "Error, the rank can't be negative"
            )
        self.__rank = value

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: Union[uuid.UUID, str]):
        if not value:
            value = uuid.uuid4()
        if isinstance(value, str):
            try:
                self.__identifier = uuid.UUID(value)
            except ValueError:
                raise AttributeError(
                    "Error on generation of the identifier")
        if isinstance(value, uuid.UUID):
            if(value.version == 4):
                self.__identifier = str(value)
            else:
                raise AttributeError("Erreur on identifier")

    def __repr__(self) -> str:
        """ function that represents a player - todo simplier l'affichage"""
        return (
            f"{self.__firstname},"
            f"{self.__lastname}, "
            f"{self.__date_of_birth}, "
            f"{self.__sexe.name}, "
            f"{self.__rank}, "
            f"{self.__identifier} "
            "\n"
        )

    def serialize(self):
        """
        function that serialize an object Player.
        In output, the function gives a dict of data
        """
        return {
                "firstname": self.firstname,
                "lastname": self.lastname,
                "date_of_birth": (self.date_of_birth.strftime("%Y-%m-%d")),
                "sexe": self.sexe.name,
                "rank": self.rank,
                "identifier": str(self.identifier)
            }
