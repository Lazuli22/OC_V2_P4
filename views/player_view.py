from views.view import View
from models.player import Player
from terminaltables import AsciiTable


class PlayersView(View):

    def show():
        pass

    def show_one_player(self, one_player: Player):
        """function that shows one player """
        table_player = (
            ("Nom", "Prénom", "Date de Naissance", "Sexe", "Classement"),
            (one_player.lastname,
                one_player.firstname,
                one_player.date_of_birth,
                one_player.sexe,
                one_player.rank))
        table_instance = AsciiTable(table_player, "Informations d'un joueur")
        table_instance.justify_columns[2] = 'left'
        print(table_instance.table)

    def show_sorted_players(self, list_players):
        """ function that shows a sorted list of players """
        table_player = [('Nom', 'Prénom', 'Classement')]
        for elt in list_players:
            table_player.append([elt.lastname, elt.firstname, elt.rank])
        table_instance = AsciiTable(table_player, "Liste triée des joueurs")
        table_instance.justify_columns[2] = 'left'
        print(table_instance.table)

    def show_all_players(self):
        """ function that shows all players the players registry """
        print("--------------------------")
        print("Liste de tous les joueurs")
        print("--------------------------")
        print("Souhaitez - vous une présentation par classement (C)")
        print("ou par ordre alphabétique (O) ?")
        res = input()
        return res

    def add_players_tournament(self, id_tournament):
        """ Function that permits to add players in a tournament """
        print("Ajoutez des joueurs à un tournoi")
        print("Au maximun il ne peut y en avoir huit")
        print("Souhaitez-vous Creer(C) ou Reprendre (S) un joueur:")
        choice = input()
        if choice == "S":
            print("Veuillez fournir l'idenfiant du joueur à reprendre")
            id_player = input()
        return choice, id_player
