from utils.player_manager import player_manager as players
from utils.tournament_manager import tournament_manager as tournaments
from controllers.mainController import MainController
from models.player import Player
import uuid

def main():
    # Create Tournements registry and Players registry
    tournaments.load_from_json()
    players.load_from_json()
    main = MainController()
    main.start()

if __name__ == "__main__":
    main()
