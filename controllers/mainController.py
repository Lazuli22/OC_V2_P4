from utils.player_manager import player_manager as players
from utils.tournament_manager import tournament_manager as tournaments
from controllers.playerController import PlayerController
from controllers.tournamentController import TournamentController
from views.menu import Menu
from views.playersView import PlayersView
from views.tournamentsView import TournamentsView


class MainController:
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
            players.save_to_json()
            tournaments.save_to_json()
            menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()

    def start_players_menu(self, input, id_player):
        """ function that shows the players menu"""
        players_menu = PlayersView()
        if input == "1":
            one_sort = players_menu.show_all_players()
            players_menu.show_sorted_players(PlayerController().players_sort(one_sort))
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
            players.save_to_json()
            tournaments.save_to_json()
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
            one_tournament = tournaments_controller.get_one(id_tournament)
            tournaments_menu.show_all_rounds(one_tournament)
            self.start()
        elif input == '5':
            one_tournament = tournaments_controller.get_one(id_tournament)
            tournaments_menu.show_all_matches(one_tournament)
            self.start()
        elif input == '6':
            self.tournament_execution()
            self.start()
        elif input == '7':
            self.start()
        elif input == '8':
            players.save_to_json()
            tournaments.save_to_json()   
            tournaments_menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()

    def tournament_execution(self):
        tournament_controller = TournamentController()
        # Select a tournament
        one_tournament = tournament_controller.select_one_tournament()
        if one_tournament.list_rounds == []:
            #add players  to a tournament
            tournament_controller.add_players_tournament(one_tournament)
            one_tournament = tournament_controller.generate_matchs_firstRound(one_tournament)
            print(type(one_tournament.list_rounds[0]))
            ## grasp scores
            tournament_controller.enter_scores_round(one_tournament)
        else:
            while(len(one_tournament.list_rounds) < 4):
                tournaments_view = TournamentsView()
                choice = tournaments_view.start_2to4_rounds()
                if choice == 'N':
                    self.start()
                    break
                else:
                    one_tournament = tournament_controller.generate_matchs_2to4Rounds(one_tournament)
                    tournament_controller.enter_scores_round(one_tournament)
                    print(one_tournament.serialize())
        
        
