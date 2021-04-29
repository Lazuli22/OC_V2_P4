from models.seriable import Serializable
from typing import Union
from models.player import Player


class Match(Serializable):
    """ Class represents a match that is characterized by
        -  name
        -  Two players
        -  a score for each player
    """

    def __init__(self, name, player1, r1, player2, r2):
        self.name = name
        self.match = {}
        if isinstance(player1, dict):
            self.match['player1'] = [Player(**player1), float(r1)]    
        elif isinstance(player1, Player):
            self.match['player1'] = [player1, float(r1)]
        else:
            raise AttributeError("Erreur sur l'instanciation d'un joueur 1 et de son résultat")
        if isinstance(player2, dict):
            self.match['player2'] = [Player(**player2), float(r2)]
        elif isinstance(player2, Player):
            self.match['player2'] = [player2, float(r2)]
        else:
            raise AttributeError("Erreur sur l'instanciation d'un joueur 2 et de son résultat")
        #print(self.match)
  
    def __repr__(self) -> str:
        """Function that represents a match"""
        return (
            f" Match entre {self.match['player1'][0].firstname} "
            f"{self.match['player1'][0].lastname}  et "
            f"{self.match['player2'][0].firstname} "
            f"{self.match['player2'][0].lastname},"
            f" ({self.match['player1'][1]},"
            f" {self.match['player2'][1]})"
            )

    def serialize(self) -> dict[str, str]:
        """
        Function serializes a match
        In output, the function gives a dict of data
        """
        return {
            'name': self.name,
            'player1': self.match["player1"][0].serialize(),
            'r1': self.match["player1"][1],
            'player2': self.match["player2"][0].serialize(),
            'r2': self.match["player2"][1]
        }
