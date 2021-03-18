from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament
from operator import attrgetter
import json


def reading_players_json():
    """function that read a json file and 
    produces a list of players
    """
    liste_players = []
    with open("players.json") as f:
        data = json.load(f)
    for elt in data:
        liste_players.append(Player(
            elt["player"]["surname"],
            elt["player"]["forename"],
            elt["player"]["date_of_birth"],
            elt["player"]["sexe"],
            elt["player"]["rank"]
        ))
    return liste_players

def main():
    #dolores_data = {'surname': 'Diaz', 'forename': 'Dolores', 'date_of_birth': '1978-08-22', 'sexe': 'Female', 'rank': 100}
    #tom_data = {"surname": "Dupond", "forname": "Tom", "date_of_birth": "1980-11-20", 'sexe': "Male", 'rank': 300}
    #dolores = Player("Diaz", "Dolores", "1978-08-22", "Female", 100)
    #tom = Player("Dupond", "Tom", "1980-11-20", "Male", 300)
    #un_match_data = Match("match 1", dolores, 0, tom, 0)
    #un_match = un_match_data.serialize()
    #print(un_match)
    #round_un_data = Round("round1", [])
    list_one_players = reading_players_json()
    tournoi_data = {"name": 'Tournoi du Monde',
                    'location': 'Paris',
                    'date': '2021-03-13',
                    'time_rule': Tournament.Time_Rule.Blitz,
                    'description': 'Tournoi de renameée mondiale qui permet qui fait affonter les meilleurs players mondiaux'
                    }
    un_tournoi = Tournament(**tournoi_data)
    un_tournoi.generate_matchs_firstRound(list_one_players)
    print(un_tournoi.serialize())


if __name__ == "__main__":
    main()
