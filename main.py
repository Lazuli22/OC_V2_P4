from models.player import Player
import json
from utils.playersFactory import PlayersFactory
from utils.tournamentsFactory import TournamentsFactory
from controllers.mainController import MainController


def reading_players_json():
    """function that reads a json file and produces a list of players """
    liste_players = []
    with open("players.json") as f:
        data = json.load(f)
    for elt in data:
        liste_players.append(Player(
            elt["player"]["firstname"],
            elt["player"]["lastname"],
            elt["player"]["date_of_birth"],
            elt["player"]["sexe"],
            elt["player"]["rank"],
            elt["player"]["identifier"]
        ))
    return liste_players


def main():
    # Create Tournements registry and Players registry
    liste_players = reading_players_json()
    tournoi_data = {"name": 'Tournoi du Monde',
                    'location': 'Paris',
                    'date': '2021-03-13',
                    'time_rule': "Blitz",
                    'description': 'Tournoi de renommée mondiale qui permet qui fait affonter les meilleurs joyeurs mondiaux'
                    }
    uneFab = TournamentsFactory()
    uneFab.create(tournoi_data)
    twoFab = PlayersFactory()
    twoFab.create(liste_players)
    main = MainController()
    main.start()


if __name__ == "__main__":
    main()
