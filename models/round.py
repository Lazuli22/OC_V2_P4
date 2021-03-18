from datetime import datetime
import re
from models.constants import REGEX
from models.player import Player
from models.match import Match
from models.seriable import Serializable


class Round(Serializable):
    """
    Class defines a round is characterized by:
        - name
        - matches list
        - star date
        - end date
    """

    def __init__(self, name, matches_list):
        self.name = name
        self.matches_list = matches_list
        self.__star_date = datetime.now()
        self.end_date = None

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
    def matches_list(self) -> list:
        return self.__matches_list

    @matches_list.setter
    def matches_list(self, matches_list: list):
        if matches_list is not None:
            self.__matches_list = matches_list

    @property
    def star_date(self) -> datetime:
        return self.__star_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date: datetime):
        self.__end_date = end_date

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
            "star_date": self.star_date,
            "end_date": self.end_date
        }

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

