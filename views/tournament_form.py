from views.form import Form
from datetime import datetime


class TournamentForm(Form):

    def createForm_one_tournament(self):
        """ function that can create a tournament"""
        dict_data = self.show("Creation d'un tournoi", [
            "Nom",
            "Lieu",
            "Date du tournoi",
            "Règle de jeu",
            "Description",
        ])
        return {
            "name": dict_data["Nom"],
            "location": dict_data["Lieu"],
            "date": dict_data["Date du tournoi"],
            "nbre_tours": 4,
            "list_rounds": [],
            "list_players": [],
            "time_rule": dict_data["Règle de jeu"],
            "description": dict_data["Description"],
            "identifier": ""
            }

    def enter_scores(self, round_one):
        """ function thats allow to enter scores """
        print(f"{round_one.name} :")
        print("Veuillez saisir les scores pour les matchs suivants:")
        for elt in round_one.matches_list:
            print(f"{elt.name} entre les joueurs : ")
            print(
                f"{elt.match['player1'][0].firstname}"
                f" {elt.match['player1'][0].lastname}"
                f" et {elt.match['player2'][0].firstname}"
                f" {elt.match['player2'][0].lastname}"
                )
            print("Veuillez saisir le score du 1er joueur :")
            elt.match["player1"][1] = float(input())
            print("Veuillez saisir le score du 2nd joueur :")
            elt.match["player2"][1] = float(input())
        print("Confirmez-vous la fin du round? (O/N)")
        res = input()
        if res == 'O':
            round_one.end_date = datetime.now()
        else:
            print("Il n'y a plus d'autres matchs")
        return round_one
