from models.constants import REGEX
from typing import Union
from models.round import Round
from enum import Enum
import uuid
import re
import datetime
from models.seriable import Serializable


class Tournament(Serializable):
    """ Clasw that defines a tournament is characterized by
    - name
    - Location
    - date
    - number of rounds
    - list of rounds
    - list players
    - time rule
    - description
    - list of dones matches
    """

    Time_Rule = Enum('TRule', 'Bullet Blitz Quick_Hit')

    def __init__(
            self,
            name,
            location,
            nbre_tours,
            list_rounds,
            list_players,
            time_rule,
            description,
            matches_dones,
            identifier,
            date=None
            ):
        errors = []
        try:
            self.name = name
        except AttributeError as e:
            errors.append(f"name:  {str(e)}")
        try:
            self.location = location
        except AttributeError as e:
            errors.append(f"location: {str(e)}")
        try:
            self.date = date
        except AttributeError as e:
            errors.append(f"date: {str(e)}")
        try:
            self.__nber_rounds = nbre_tours
        except AttributeError as e:
            errors.append(f"nombre de tours: {str(e)}")
        try:
            self.list_rounds = list_rounds
        except AttributeError as e:
            errors.append(f"liste de rounds :{str(e)}")
        try:
            self.list_players = list_players
        except AttributeError as e:
            errors.append(f"liste de joueurs : {str(e)}")
        try:
            self.time_rule = time_rule
        except AttributeError as e:
            errors.append(f"règle de jeu: {str(e)}")
        try:
            self.description = description
        except AttributeError as e:
            errors.append(f"description: {str(e)}")
        date = str(self.date)
        self.identifier = identifier if identifier else \
            f"{self.name}_{self.location}_{date}"
        self.matches_dones = matches_dones

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if re.search(REGEX, value):
            self.__name = value
        else:
            print(
                "Attention the name tournament"
                "includes other things than letters !"
            )

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        if re.search(REGEX, value):
            self.__location = value
        else:
            print(
                "Attention the location name"
                "includes other thnings thant letters!"
                )

    @ property
    def date(self) -> datetime.date:
        return self.__date

    @date.setter
    def date(self, dateT: Union[str, datetime.date]):
        if dateT is None:
            self.date = datetime.date.now()
        try:
            if isinstance(dateT, str):
                dateT = datetime.date.fromisoformat(dateT)
                self.__date = dateT
        except ValueError:
            raise AttributeError("Impossible de determiner la date")
        try:
            if isinstance(dateT, datetime.date):
                self.__date = dateT
        except ValueError:
            raise AttributeError("Impossible de determiner la date")

    @property
    def list_rounds(self) -> list[Round]:
        return self.__list_rounds

    @list_rounds.setter
    def list_rounds(self, list_rounds: list[Union[dict, Round]]):
        self.__list_rounds = []
        for elt in list_rounds:
            if isinstance(elt, dict):
                one_round = Round(**elt)
                self.__list_rounds.append(one_round)
            elif isinstance(elt, Round):
                self.__list_rounds.append(elt)
            else:
                raise AttributeError("Erreur sur la création d'un Round")

    @property
    def list_players(self) -> list[uuid.UUID]:
        return self.__list_players

    @list_players.setter
    def list_players(self, new_players: list[uuid.UUID]):
        self.__list_players = []
        if new_players is not None:
            if len(new_players) != 8:
                raise AttributeError("Erreur sur les joueurs")
            self.__list_players = new_players

    @property
    def time_rule(self):
        return self.__time_rule

    @time_rule.setter
    def time_rule(self, value: Union[Time_Rule, str]):
        if isinstance(value, str):
            try:
                self.__time_rule = Tournament.Time_Rule[value]
            except KeyError:
                raise AttributeError("Impossible to determine  the rule time")
        if isinstance(value, Tournament.Time_Rule):
            try:
                self.__time_rule = value
            except KeyError:
                raise AttributeError(
                    "The value must be Tournament.Time_Rule ou str"
                )

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if description is not None:
            self.__description = description

    def serialize(self):
        """ Function that seralizes a tournament.
            In output, it gives a dict of data keys/values
        """
        list_rounds = []
        list_matches_dones = []
        for elt in self.list_rounds:
            list_rounds.append(elt.serialize())
        for elt in self.matches_dones:
            list_matches_dones.append(str(elt))
        return {
                "name": self.name,
                "location": self.location,
                "date": self.date.strftime("%Y-%m-%d"),
                "nbre_tours": 4,
                "list_rounds": list_rounds,
                "list_players": self.list_players,
                "time_rule": self.time_rule.name,
                "description": self.description,
                "matches_dones": list_matches_dones,
                "identifier": self.identifier
                }

    def __repr__(self) -> str:
        """ function that represents a tournament """
        return (
            f"{self.name},"
            f"{self.location}, "
            f"{self.date}, "
            f"{self.list_rounds}, "
            f"{self.list_players}, "
            f"{self.time_rule.name}, "
            f"{self.matches_dones}, "
            f"{self.description}, "
            f"{self.identifier} "
            "\n"
        )
