from views.form import Form


class PlayerForm(Form):

    def createForm_one_player(self):
        """ function that can create a player"""
        dict_data = self.show("Creation d'un joueur", [
            "Prénom",
            "Nom",
            "Date de naissance",
            "Sexe",
            "Classement",
        ])
        return {
            "firstname": dict_data["Prénom"],
            "lastname": dict_data["Nom"],
            "date_of_birth": dict_data["Date de naissance"],
            "sexe": dict_data["Sexe"],
            "rank": dict_data["Classement"]
        }

    def modifyForm_one_player(self, one_player):
        """ fonction that modifies a rank player """
        new_rank = 0
        print("Veuillez fournir le nouveau classement du joueur : ")
        print(f"{one_player.firstname} {one_player.lastname}")
        new_rank = input()
        one_player.rank = int(new_rank)
     

            