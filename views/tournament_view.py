from views.view import View
from models.round import Round
from models.match import Match
from models.tournament import Tournament
from utils.tournament_manager import tournament_manager as tournaments
from terminaltables import AsciiTable


class TournamentView(View):

    def show():
        pass

    def show_one_match(self, match: Match):
        """ function that shows detail of a match """
        print(match)

    def show_all_matches(self, tournament: Tournament):
        """ function that shows all matches of a tournament """
        list_matches = []
        print("Liste de tous les matchs d'un tounoi :")
        for elt in tournament.list_rounds:
            for e in elt.matches_list:
                list_matches.append(e)
        for elt in list_matches:
            self.show_one_match(elt)

    def show_one_round(self, round: Round):
        """ function that shows element of a round """
        print("Détail d'un tour :")
        print(f"{round.name}")
        print(f"date de début: {round.start_date}")
        for elt in round.matches_list:
            print(elt)
        print(f"date de fin: {round.end_date}")

    def show_all_rounds(self, tournament: Tournament):
        """ function that shows all rounds of a tournament """
        print("Liste de tous les tours d'un tounoi :")
        for elt in tournament.list_rounds:
            print("--------------------")
            self.show_one_round(elt)
            print("--------------------")

    def show_one_tournament(self, tournament: Tournament):
        """ function that shows elements of a tournament"""
        print("-----------------------")
        print("Détail d'un tournoi :")
        print(f"Tournoi n°{tournament.identifier}, de nom : {tournament.name}")
        print(f"Règle de jeu : {tournament.time_rule.name}")
        print(f"Date du tournoi : {tournament.date}")
        print(f"Liste des tours : {tournament.list_rounds}")
        print(f"Liste de joueurs : {tournament.list_players}")
        print(f"Description : {tournament.description}")

    def show_all_tournaments(self):
        """ function thats shows all tournaments of the registry"""
        all_tournaments = tournaments.find_all()
        list_tournaments = [("Nom", "Lieu", "Date", "Règle de jeu", "Description")]
        for elt in all_tournaments:
            list_tournaments.append(
                            [elt.name,
                                elt.location,
                                elt.date,
                                elt.time_rule.name,
                                elt.description])
        table_instance = AsciiTable(list_tournaments, "Liste des tournois")
        print(table_instance.table)

    def show_initialize_players(self):
        """ function that initialize the list of players"""
        print("Souhaitez-vous initialiser la liste des joueurs un à un (U) ou via un fichier(F)")
        choice = input()
        return choice

    def id_players_file(self):
        """ function can enter a id players file """
        print("Veuillez fournir le fichier des joueurs:")
        file = input()
        return file

    def start_2to4_rounds(self):
        """function that  """
        print("Souhaitez - vous poursuivre le suivi d'exécution du tournoi (O/N) ?")
        choice = input()
        return choice

    def show_tournament_done(self, one_tournament: Tournament):
        print(" ------------------------------------------------------")
        print(f" {one_tournament.name} du {one_tournament.date} terminé")
        print(f"Description du tournoi : {one_tournament.description}")
