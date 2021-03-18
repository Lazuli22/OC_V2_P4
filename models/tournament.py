from models.constants import REGEX
from typing import Union
from models.player import Player
from models.match import Match
from models.round import Round
from enum import Enum
import uuid
import re
import datetime
from operator import attrgetter
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
    """

    Time_Rule = Enum('TRule', 'Bullet Blitz Quick_Hit')

    def __init__(
            self,
            name,
            location,
            date,
            time_rule,
            description
            ):
        self.name = name
        self.location = location
        self.date = date
        self.__nber_rounds = 4
        self.__list_rounds = []
        self.list_players = []
        self.time_rule = time_rule
        self.description = description
        date = str(self.date)
        self.identifier = f"{self.name}_{self.location}_{date}"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if re.search(REGEX, value):
            self.__name = value
        else:
            print("Attention the name tournament includes other things than letters !")

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        if re.search(REGEX, value):
            self.__location = value
        else:
            print("Attention the location name includes other thnings thant letters!")

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
            raise AttributeError("Impossible to determine la date")
        try:
            if isinstance(dateT, datetime.date):
                self.__date = dateT
        except ValueError:
            raise AttributeError("Impossible to determine la date")

    @property
    def list_rounds(self) -> list[Round]:
        return self.__list_rounds

    @list_rounds.setter
    def list_rounds(self, list_rounds: list[Round]):
        if list_rounds is not None:
            self.__list_rounds = list_rounds

    @property
    def list_players(self) -> list[uuid.UUID]:
        return self.__list_players

    @list_players.setter
    def list_players(self, new_players: list[uuid.UUID]):
        if new_players is not None:
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
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if description is not None:
            self.__description = description

    def list_identifiers_players(liste_players):
        """ function that gives a list id of players """
        list_id_players = []
        for elt in liste_players:
            list_id_players.append(elt.identifier)
        return list_id_players

    def generate_matchs_firstRound(self, list_players):
        """ function that generates matchs for the 1er Round """
        list_triee = sorted(
                    list_players,
                    key=attrgetter("rank"),
                    reverse=True
                    )
        self.list_rounds.append(Round("Round 1", [
            Match("Match1", list_triee[0], 0, list_triee[4], 0),
            Match("Match2", list_triee[1], 0, list_triee[5], 0),
            Match("Match3", list_triee[2], 0, list_triee[6], 0),
            Match("Match4", list_triee[3], 0, list_triee[7], 0)
            ]))
        for elt in list_players:
            self.list_players.append(elt.identifier)

    def serialize(self):
        """ Function that seralizes a tournament.
            In output, it gives a dict of data keys/values
        """
        list_rounds = []
        for elt in self.list_rounds:
            list_rounds.append(elt.serialize())
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%Y-%m-%d"),
            "nbre_tours": 4,
            "rounds": list_rounds,
            "list_players": self.list_players,
            "time_rule": self.time_rule.value,
            "description": self.description,
            "identifier": self.identifier
        }




