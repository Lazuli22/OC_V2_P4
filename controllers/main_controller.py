from utils.player_manager import player_manager as players
from utils.tournament_manager import tournament_manager as tournaments
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.menu import Menu
from views.player_view import PlayersView
from views.tournament_view import TournamentView


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
            menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()
        players.save_to_dbase()
        tournaments.save_to_dbase()

    def start_players_menu(self, input, id_player):
        """ function that shows the players menu"""
        players_menu = PlayersView()
        if input == "1":
            one_sort = players_menu.show_all_players()
            players_menu.show_sorted_players(
                        PlayerController().players_sort(one_sort, None)
                        )
            self.start()
        elif input == "2":
            one_player = PlayerController().get_one(id_player)
            players_menu.show_one_player(one_player)
            self.start()
        elif input == "3":
            one_player = PlayerController().modify_one_player(id_player)
            players_menu.show_one_player(one_player)
            self.start()
        elif input == "4":
            PlayerController().create_one()
            self.start()
        elif input == "5":
            self.start()
        elif input == "6":
            players_menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()
        players.save_to_dbase()
        tournaments.save_to_dbase()

    def start_tournaments_menu(self, input, id_tournament):
        """ function that stars the tournaments menu"""
        tournaments_menu = TournamentView()
        tournaments_controller = TournamentController()
        if input == '1':
            tournaments_menu.show_all_tournaments()
            self.start()
        elif input == '2':
            one_tournament = tournaments_controller.create_one()
            tournaments_menu.show_one_tournament(one_tournament)
            self.start()
        elif input == '3':
            one_tournament = tournaments_controller.get_one(id_tournament)
            tournaments_menu.show_one_tournament(one_tournament)
            self.start()
        elif input == '4':
            one_tournament = tournaments_controller.get_one(id_tournament)
            one_sort = PlayersView().show_all_players()
            PlayersView().show_sorted_players(
                        PlayerController().players_sort(one_sort, one_tournament)
                        )
            self.start()
        elif input == '5':
            one_tournament = tournaments_controller.get_one(id_tournament)
            tournaments_menu.show_all_rounds(one_tournament)
            self.start()
        elif input == '6':
            one_tournament = tournaments_controller.get_one(id_tournament)
            tournaments_menu.show_all_matches(one_tournament)
            self.start()
        elif input == '7':
            self.tournament_execution()
            self.start()
        elif input == '8':
            self.start()
        elif input == '9':
            tournaments_menu.quit()
        else:
            print("Veuillez choisir une option valide du menu")
            self.start()
        players.save_to_dbase()
        tournaments.save_to_dbase()

    def tournament_execution(self):
        """ function that executes the tournament"""
        tournament_controller = TournamentController()
        one_tournament = tournament_controller.select_one_tournament()
        if one_tournament.list_rounds == []:
            tournament_controller.add_players_tournament(one_tournament)
            one_tournament = tournament_controller.generate_matchs_firstRound(
                            one_tournament
                            )
            tournament_controller.enter_scores_round(one_tournament)
            scored_ranking = tournament_controller.players_ranking(one_tournament)
            TournamentView().show_players_ranking(scored_ranking)
        else:
            while(len(one_tournament.list_rounds) < 4):
                choice = TournamentView().start_2to4_rounds()
                if choice == 'N':
                    self.start()
                    break
                else:
                    one_tournament = tournament_controller.matchs_2to4Rounds(
                        one_tournament
                        )
                    tournament_controller.enter_scores_round(one_tournament)
                    scored_ranking = tournament_controller.players_ranking(
                        one_tournament
                        )
                    TournamentView().show_players_ranking(scored_ranking)
        players.save_to_dbase()
        tournaments.save_to_dbase()
