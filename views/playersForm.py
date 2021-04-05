from views.form import Form
from models.player import Player


class PlayersForm(Form):

    def createForm_one_player(self):
        """ function that can create a player"""
        dict_data = self.show("Creation d'un joueur", [
            "Prénom",
            "Nom",
            "Date de naissance",
            "Sexe",
            "Classement",
        ])
        return Player(
            dict_data["Prénom"],
            dict_data['Nom'],
            dict_data["Date de naissance"],
            dict_data["Sexe"],
            dict_data["Classement"],
            ""
        )
