from models.player import Player
import json
from models.playersFactory import PlayersFactory
from models.tournamentsFactory import TournamentsFactory



def reading_players_json():
    """function that read a json file and 
    produces a list of players
    """
    liste_players = []
    with open("players.json") as f:
        data = json.load(f)
    for elt in data:
        liste_players.append(Player(
            elt["player"]["firstname"],
            elt["player"]["lastname"],
            elt["player"]["date_of_birth"],
            elt["player"]["sexe"],
            elt["player"]["rank"]
        ))
    return liste_players


def main():
    # Create Tournements registry and Players registry
    liste_players = reading_players_json()
    tournoi_data = {"name": 'Tournoi du Monde',
                'location': 'Paris',
                'date': '2021-03-13',
                'time_rule': Tournament.Time_Rule.Blitz,
                'description': 'Tournoi de renameée mondiale qui permet qui fait affonter les meilleurs players mondiaux'
                }
    TournamentsFactory(tournoi_data)
    PlayersFactory().create(liste_players)



if __name__ == "__main__":
    main()
