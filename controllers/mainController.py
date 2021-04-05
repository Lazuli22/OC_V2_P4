from utils.singleton import Singleton
from controllers.playerController import PlayerController
from controllers.tournamentController import TournamentController
from views.menu import Menu
from views.playersView import PlayersView
from views.tournamentsView import TournamentsView


class MainController(Singleton):
    """
    main controller class that permits to start the program
    """

    def __init__(self):
        pass

    def start(self):
        """ 1er function of the program """
        menu = Menu()
        one_input = menu.show_main_menu()
        if one_input == '1':
            two_input, id_player = menu.show_players_menu()
            self.start_players_menu(two_input, id_player)
        elif one_input == '2':
            input_two, id_tournament = menu.show_tournaments_menu()
            self.start_tournaments_menu(input_two, id_tournament)
        elif one_input == '3':
            menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()

    def start_players_menu(self, input, id_player):
        """ function that shows the players menu"""
        players_menu = PlayersView()
        if input == "1":
            players_menu.show_all_players()
            self.start()
        elif input == "2":
            one_player = PlayerController().get_one(id_player)
            players_menu.show_one_player(one_player)
            self.start()
        elif input == "3":
            PlayerController().create_one_player()
            self.start()
        elif input == "4":
            self.start()
        elif input == "5":
            players_menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()
            
    def start_tournaments_menu(self, input, id_tournament):
        """ function that stars the tournaments menu"""
        tournaments_menu = TournamentsView()
        tournaments_controller = TournamentController()
        if input == '1':
            tournaments_menu.show_all_tournaments()
            self.start()
        elif input == '2':
            one_tournament = tournaments_controller.get_one(id_tournament)
            tournaments_menu.show_one_tournament(one_tournament)
            self.start()
        elif input == '3':
            one_tournament = tournaments_controller.create_one_tournement()
            tournaments_menu.show_one_tournament(one_tournament)
            self.start()
        elif input == '4':
            self.tournament_execution()
            self.start()
        elif input == '5':
            self.start()
        elif input == '6':
            tournaments_menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()

    def tournament_execution(self):
        tournaments_view = TournamentsView()
        tournament_controller = TournamentController()
        players_controller = PlayerController
        choice, id_tournament = tournaments_view.show_load_create("tournoi")
        one_tournament = tournament_controller.load_create(choice, id_tournament)
        nber_players = len(one_tournament.list_players)
        if nber_players <= 8:
            nb = 0
            choice = tournaments_view.show_initialize_players()
            if choice == 'U':
                while nb <= 7:
                    choice, id_player = tournaments_view.show_load_create("joueur")    
                    one_player = players_controller.load_create(choice, id_player)
                    print(one_player)
                    one_tournament.list_players.append(one_player.identifier)
                    nb = nb+1
                print(one_tournament.list_players)
            else:
                file = tournaments_view.id_players_file()
                one_tournament.list_players = players_controller.reading_players_json(file)
                print(one_tournament.list_players)
        tournament_controller.generate_matchs_firstRound(one_tournament)
        print(one_tournament.list_rounds)
    
        ## Puis saisie les résultats
        ## Regéner les 3 autres tours.