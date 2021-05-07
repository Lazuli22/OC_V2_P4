from views.view import View


class Menu(View):

    def show(self, titre, options):
        """ function that shows a menu"""
        print(titre)
        print("Que souhaitez-vous faire ? :")
        for k, option in enumerate(options, start=1):
            print(f"{k} - {option}")

    def show_main_menu(self):
        """ function that shows the main menu """
        self.show(
            "----------------------------------------------------------\n"
            "| Bienvenue sur l'outil de gestion des tournois d'echecs |\n"
            "----------------------------------------------------------\n",
            ["Gérer les joueurs",
             "Gérer les tournois",
             "Quitter"]
            )
        one_input = input()
        return one_input

    def show_tournaments_menu(self):
        """function that shows the tournaments menu """
        id_tournament = ""
        self.show(
            "---------------------\n"
            "| Menu des tournois |\n"
            "---------------------\n",
            ["Consulter tous les tournois ",
             "Consulter un tournoi en particulier",
             "Créer un tournoi",
             "Consulter tous les rounds d'un tournoi",
             "Consulter tous les matchs d'un tournoi",
             "Suivre la réalisation d'un tournoi",
             "Revenir au menu précédent",
             "Quitter",
             ]
            )
        one_input = input()
        if one_input in ["2", "4", "5"]:
            print("Veuillez fournir l'idenfiant du tournoi à consulter :")
            id_tournament = input()
        elif one_input == "3":
            print("Ajout d'un tournoi sein du registre des tournois")
        return (one_input, id_tournament)

    def show_players_menu(self):
        """function that shows the players menu """
        id_player = ""
        self.show(
            "--------------------\n"
            "| Menu des joueurs |\n"
            "--------------------\n",
            ["Consulter tous les joueurs",
             "Consulter un joueur en particulier",
             "Modifier le classement d'un joueur en particulier",
             "Créer un joueur",
             "Revenir au menu précédent",
             "Quitter"]
            )
        one_input = input()
        if one_input == "2" or one_input == "3":
            print("Veuillez fournir l'idenfiant du joueur à consulter/modifier :")
            id_player = input()
        elif one_input == "4":
            print("Ajout d'un joueur au sein du registre des joueurs")
        return (one_input, id_player)