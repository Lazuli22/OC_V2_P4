from utils.player_manager import player_manager as players
from utils.tournament_manager import tournament_manager as tournaments
from controllers.main_controller import MainController


def main():
    # Create Tournements registry and Players registry
    tournaments.load_from_dbase()
    players.load_from_dbase()
    main = MainController()
    main.start()


if __name__ == "__main__":
    main()
