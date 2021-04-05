from views.form import Form
from models.tournament import Tournament


class TournamentsForm(Form):

    def createForm_one_tournament(self):
        """ function that can create a tournament"""
        dict_data = self.show("Creation d'un tournoi", [
            "Nom",
            "Lieu",
            "Date du tournoi",
            "Règle de jeu",
            "Description",
        ])
        return Tournament(
            dict_data["Nom"],
            dict_data["Lieu"],
            dict_data["Date du tournoi"],
            dict_data["Règle de jeu"],
            dict_data["Description"]
            )
