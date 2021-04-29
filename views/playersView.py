from views.view import View
from models.player import Player
from utils.player_manager import player_manager as players


class PlayersView(View):

    def show():
        pass

    def show_one_player(self, one_player: Player):
        """function that shows one player """
        print("")
        print(f"Détail du joueur {one_player.firstname} {one_player.lastname}")
        print(f"date de naissance: {one_player.date_of_birth}")
        print(f"sexe: {one_player.sexe}")
        print(f"classement: {one_player.rank}")
        print(f"identifiant: {one_player.identifier}")
        print("")

    def show_sorted_players(self, list_players):
        """ function that shows a sorted list of players """
        print("--------------------------")
        print("Liste triée des joueurs ")
        print("--------------------------")
        for elt in list_players:
            print(f"{elt.firstname} {elt.lastname} {elt.rank}")


    def show_all_players(self):
        """ function that shows all players the players registry """
        print("--------------------------")
        print("Liste de tous les joueurs")
        print("--------------------------")
        print("Souhaitez - vous une présentation par classement (C) ou par ordre alphabétique (O) ?")
        res = input()
        return res

    def add_players_tournament(self, id_tournament):
        """ Function that permits to add players in a tournament """
        print("Ajoutez des joueurs à un tournoi")
        print("Au maximun il ne peut y en avoir huit")
        nber_players = len()
        print("Souhaitez-vous Creer(C) ou Reprendre (S) un joueur:")
        choice = input()
        if choice == "S":
            print("Veuillez fournir l'idenfiant du joueur à reprendre")
            id_player = input()
        return choice, id_player
















