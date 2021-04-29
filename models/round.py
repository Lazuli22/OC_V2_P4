from datetime import datetime
import re
from models.constants import REGEX
from models.seriable import Serializable
from typing import Union
from models.match import Match


class Round(Serializable):
    """
    Class defines a round is characterized by:
        - name
        - matches list
        - star date
        - end date
    """

    def __init__(self, name, matches_list, start_date, end_date):
        self.name = name
        #print(self.name)
        self.matches_list = matches_list
        #print(self.matches_list)
        self.start_date = start_date
        #print(self.start_date)
        self.end_date = end_date
        #print(self.end_date)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if re.search(REGEX, value):
            self.__name = value
        else:
            raise AttributeError(
                "Attention  the name includes other things than letters !"
            )

    @property
    def matches_list(self) -> list[Match]:
        return self.__matches_list

    @matches_list.setter
    def matches_list(self, matches_list: list[Union[dict, Match]]):
        self.__matches_list = []
        for elt in matches_list:
            if isinstance(elt, dict):
                self.__matches_list.append(Match(**elt))
            elif isinstance(elt, Match):
                self.__matches_list.append(elt)
            else:
                raise AttributeError("Erreur sur la création d'un Match")
        #print(self.matches_list)

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date: Union[str, datetime]):
        if not start_date:
            self.__start_date = datetime.now()
        else:
            if isinstance(start_date, str):
                try:
                    self.__start_date = datetime.fromisoformat(start_date)
                except ValueError:
                    raise AttributeError("impossible to determine the date")
            elif isinstance(start_date, datetime):
                self.__start_date = start_date
            else:
                raise AttributeError("Impossible de déterminer la date")

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date: Union[str, datetime]):
        if not end_date:
            self.__end_date = datetime.now()
        else:
            if isinstance(end_date, str):
                try:
                    self.__end_date = datetime.fromisoformat(end_date)
                except ValueError:
                    raise AttributeError("impossible to determine the date")
            elif isinstance(end_date, datetime):
                self.__end_date = end_date
            else:
                raise AttributeError("Impossible de déterminer la date")

    def serialize(self) -> dict[str, str]:
        """ 
        function that serializes a round and
        in output gives a dict of data
        """
        matches_list = []
        for elt in self.matches_list:
            matches_list.append(elt.serialize())
        return {
            "name": self.name,
            "matches_list": matches_list,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat()
        }
