from models.seriable import Serializable


class Match(Serializable):
    """ Class represents a match that is characterized by
        -  name
        -  Two players
        -  a score for each player
    """

    def __init__(self, name, player1, r1, player2, r2):
        self.name = name
        self.match = {}
        self.match['player1'] = [player1, r1]
        self.match['player2'] = [player2, r2]

    def __repr__(self) -> str:
        """Function that represents a match"""
        return (
            f"<match entre {self.match['player1'][0]} et"
            f"{self.match['player2'][0]},"
            f"score de player 1 ={self.match['player1'][1]},"
            f"score de player 2 = {self.match['player2'][1]}>"
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
