from operator import itemgetter, attrgetter
from itertools import combinations
from views.tournamentsView import TournamentsView
from views.tournamentsForm import TournamentsForm
from controllers.controller import Controller
from controllers.playerController import PlayerController
from models.match import Match
from models.round import Round
from utils.tournament_manager import tournament_manager as tournaments


class TournamentController(Controller):

    def create_one_tournement(self):
        """ function that creates a new tournement """
        form = TournamentsForm()
        one_tournament = form.createForm_one_tournament()
        the_tournament = tournaments.create(**one_tournament)
        return the_tournament

    def get_one(self, id_tournament):
        """ function that gets a specific Tournament """
        one_tournament = tournaments.find_by_id(id_tournament)
        return one_tournament

    def load_create(self, choice, id_element):
        if choice == 'C':
            one_tournament = self.create_one_tournement()
        else:
            if choice == "R":
                one_tournament = self.get_one(id_element)
            else:
                raise(Exception("Veuillez choisir une option valide"))
        return one_tournament

    def select_one_tournament(self):
        tournaments_view = TournamentsView()
        choice, id_tournament = tournaments_view.show_load_create("tournoi")
        one_tournament = self.load_create(choice, id_tournament)
        return one_tournament

    def add_players_tournament(self, one_tournament):
        tournaments_view = TournamentsView()
        nber_players = len(one_tournament.list_players)
        if nber_players <= 8:
            nb = 0
            choice = tournaments_view.show_initialize_players()
            if choice == 'U':
                while nb <= 7:
                    choice, id_player = tournaments_view.show_load_create("joueur")    
                    one_player = PlayerController().load_create(choice, id_player)
                    one_tournament.list_players.append(one_player.identifier)
                    nb = nb+1
                print(one_tournament.list_players)
            else:
                file = tournaments_view.id_players_file()
                one_tournament.list_players = PlayerController().reading_players_json(file)
                print(one_tournament.list_players)

    def generate_matchs_firstRound(self, tournament):
        """ function that generates matchs for the 1er Round """
        list_players = tournament.list_players
        all_list_players = []
        players_controller = PlayerController()
        for elt in list_players:
            all_list_players.append(players_controller.get_one(elt))
        list_triee = sorted(
                    all_list_players,
                    key=attrgetter("rank"),
                    reverse=True
                    )
        tournament.matches_dones += [
                list_triee[0].identifier+":"+list_triee[4].identifier,
                list_triee[1].identifier+":"+list_triee[5].identifier,
                list_triee[2].identifier+":"+list_triee[6].identifier,
                list_triee[3].identifier+":"+list_triee[7].identifier
            ]
        tournament.list_rounds.append(Round("Round 1", [
            Match("Match1", list_triee[0], 0, list_triee[4], 0),
            Match("Match2", list_triee[1], 0, list_triee[5], 0),
            Match("Match3", list_triee[2], 0, list_triee[6], 0),
            Match("Match4", list_triee[3], 0, list_triee[7], 0)
            ], "", ""))
        return tournament

    #Saisie des résultats
    def enter_scores_round(self, one_tournament):
        """ function thats can enter scores of a round """
        list_rounds = one_tournament.list_rounds
        tournaments_form = TournamentsForm()
        tournaments_form.enter_scores(list_rounds[-1])

    def diff_list_matches(self, l1, l2):
        list_diff = list(set(l1) - set(l2))
        return list_diff

    def give_next_match(self, one_player, sorted_list, matches_allowed):
        id_player1 = str(one_player[0].identifier)
        print(id_player1)
        if sorted_list is not None:
            for elt in sorted_list:
                id_player2 = str(elt[0].identifier)
                print(id_player2)
                match_plays = []
                #print(sorted_list)
                if self.sort_two_players(id_player1, id_player2) in matches_allowed:
                    match_plays.append(one_player)
                    match_plays.append(elt)
                    return match_plays

    def sort_two_players(self, p1, p2):
        return f"{min(p1, p2)}:{max(p1, p2)}"

    def generate_matchs_2to4Rounds(self, tournament):
        all_list_players = []
        list_triee = []
        #players_controller = PlayerController()
        nbre_tours = len(tournament.list_rounds)
        if nbre_tours > 0:
            thelast_round = tournament.list_rounds[-1]
            list_matches = thelast_round.matches_list
            for elt in list_matches:
                dict_part1 = (
                                elt.match['player1'][0],
                                elt.match['player1'][0].rank,
                                elt.match['player1'][1],
                                
                )
                all_list_players.append(dict_part1)
                dict_part2 = (
                            elt.match['player2'][0],
                            elt.match['player2'][0].rank,
                            elt.match['player2'][1]
                )
                all_list_players.append(dict_part2)
                
                list_triee = sorted(
                    all_list_players,
                    key=itemgetter(2, 1),
                    reverse=True
                )
        sorted_only_players = []
        for elt in list_triee:
            sorted_only_players.append([elt[0], elt[2]])
        print(sorted_only_players)
        matches_list = tournament.list_players
        matches_dones = tournament.matches_dones
        matches_comb = [f"{min(p1, p2)}:{max(p1, p2)}"for p1, p2 in combinations(matches_list, 2)]
        #print(len(matches_comb))
        matches_diff = self.diff_list_matches(matches_comb, matches_dones)
        #print(len(matches_diff))
        matches_for_next_round = []
        while len(sorted_only_players) > 2:
            elt = sorted_only_players[0]
            res = self.give_next_match(elt, sorted_only_players, matches_diff)
            matches_for_next_round.append(res)
            print("match selectionné :")
            print(res)
            print("--------------------")
            sorted_only_players.remove(res[0])
            sorted_only_players.remove(res[1])
            print(sorted_only_players)
        matches_for_next_round.append(sorted_only_players)
        print(matches_for_next_round)
        all_new_matches = []
        tournament.matches_dones += [
            str(matches_for_next_round[0][0][0].identifier)+":"+str(matches_for_next_round[0][1][0].identifier),
            str(matches_for_next_round[1][0][0].identifier)+":"+str(matches_for_next_round[1][1][0].identifier),
            str(matches_for_next_round[2][0][0].identifier)+":"+str(matches_for_next_round[2][1][0].identifier),
            str(matches_for_next_round[3][0][0].identifier)+":"+str(matches_for_next_round[3][1][0].identifier)
        ]   

        print(matches_for_next_round[0][0])
        all_new_matches.append(Match("Match1", matches_for_next_round[0][0][0], matches_for_next_round[0][0][1], matches_for_next_round[0][1][0], matches_for_next_round[0][1][1]))
        all_new_matches.append(Match("Match 2", matches_for_next_round[1][0][0], matches_for_next_round[1][0][1], matches_for_next_round[1][1][0], matches_for_next_round[1][1][1]))
        all_new_matches.append(Match("Match 3", matches_for_next_round[2][0][0], matches_for_next_round[2][0][1], matches_for_next_round[2][1][0], matches_for_next_round[2][1][1]))
        all_new_matches.append(Match("Match 4", matches_for_next_round[3][0][0], matches_for_next_round[3][0][1], matches_for_next_round[3][1][0], matches_for_next_round[3][1][1]))
        tournament.list_rounds.append(Round(f"Round {nbre_tours+1}", all_new_matches, thelast_round.start_date, thelast_round.end_date))
        for elt in tournament.list_rounds:
            print(elt.serialize())
        print(len(tournament.list_rounds))
        return tournament
