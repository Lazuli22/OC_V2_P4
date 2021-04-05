from views.view import View
from models.round import Round
from models.match import Match
from utils.tournamentsFactory import TournamentsFactory


class TournamentsView(View):

    def show():
        pass

    def show_one_match(self, match: Match):
        """ function that shows detail of a match """
        print("Détail d'un match :")
        print(f"Match {match.name}")
        print("qui oppose les joueurs suivants")
        print(f"joueur {match['player1']}")
        print(f"joueur {match['player2']}")

    def show_one_round(self, round: Round):
        """ function that shows element of a round """
        print("Détail d'un round :")
        print(f"Round {round.name}")
        print(f"date de début {round.star_date}")
        for elt in round.matches_list:
            self.show_one_match(elt)
        
    def show_all_rounds(self, tournament):
        """ function that shows all rounds of a tournament """
        print("Liste de tous les tours d'un tounoi :")
        for elt in tournament.list_rounds:
            print("--------------------")
            self.show_one_round(elt)
            print("--------------------")

    def show_one_tournament(self, tournament):
        """ function that shows elements of a tournament"""
        print("")
        print("Détail d'un tournoi :")
        print(f"Tournoi n°{tournament.identifier}, de nom : {tournament.name}")
        print(f"Règle de jeu : {tournament.time_rule.name}")
        print(f"Date du tournoi : {tournament.date}")
        print(f"Liste des tours : {tournament.list_rounds}")
        print(f"Liste de joueurs : {tournament.list_players}")
        print(f"Description : {tournament.description}")

    def show_all_tournaments(self):
        """ function thats shows all tournaments of the registry"""
        the_factory = TournamentsFactory.getInstance()
        print("Liste de tous les tournois")
        for elt in the_factory.tournaments_registry:
            print("---------------------------------")
            self.show_one_tournament(elt)
            print("---------------------------------")

    def show_initialize_players(self):
        """ function that initialize the list of players"""
        print("Souahitez vous initialiser la liste des joueurs un à un (U) ou via un fichier(F)")
        choice = input()
        return choice

    def id_players_file(self):
        """ function that gives a id players file """   
        print("Veuillez fournir le fichier des identifiants de joueurs:")
        file = input()
        return file











