import datetime
import re
import uuid
from enum import Enum
from typing import Union
from models.seriable import Serializable
from models.constants import REGEX


class Player(Serializable):
    """ Class define a player who is characteriszed :
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
            rank=0
            ):
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank
        self.identifier = uuid.uuid4()


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
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, value: int):
        if int(value) < 0:
            raise AttributeError(
                "Error, the rank can't be negative"
            )
        self.__rank = value

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: Union[uuid.UUID, str]):
        if isinstance(value, str):
            try:
                self.__identifier = uuid.uuid4(value)
            except ValueError:
                raise AttributeError(
                    "Error on generation of the identifier")
        if isinstance(value, uuid.UUID):
            if(value.version == 4):
                self.__identifier = str(value)
        else:
            raise AttributeError("Erreur on identifier")

    def __repr__(self) -> str:
        """ function that represents a player"""
        return (
            f"<Player {self.__firstname},"
            f"{self.__lastname},"
            f"(date of birth = {self.__date_of_birth},"
            f"sexe = {self.__sexe},"
            f"rank = {self.__rank},"
            f"identifier = {self.__identifier})>"
        )

    def serialize(self):
        """ 
        function that serialize an object Player.
        In output, the function gives a dict of data
        """
        return {
                "firstname": self.firstname,
                "lastname": self.lastname,
                "date_of_birth": self.date_of_birth.strftime("%Y-%m-%d"),
                "sexe": self.sexe.name,
                "rank": self.rank,
                "identifier": self.identifier
            }
