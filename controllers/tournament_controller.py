from operator import itemgetter, attrgetter
from itertools import combinations
from views.tournament_view import TournamentView
from views.player_view import PlayersView
from views.tournament_form import TournamentForm
from controllers.controller import Controller
from controllers.player_controller import PlayerController
from models.match import Match
from models.round import Round
from models.tournament import Tournament
from utils.tournament_manager import tournament_manager as tournaments
from utils.player_manager import player_manager as players


class TournamentController(Controller):

    def create_one(self):
        """ function that creates a new tournement """
        one_tournament = TournamentForm().createForm_one_tournament()
        the_tournament = tournaments.create(**one_tournament)
        return the_tournament

    def get_one(self, id_tournament):
        """ function that gets a specific Tournament """
        one_tournament = tournaments.find_by_id(id_tournament)
        return one_tournament

    def load_create(self, choice, id_element):
        """ function that gives the choice to create or load a tournamenent"""
        if choice == 'C':
            one_tournament = self.create_one()
        else:
            if choice == "R":
                one_tournament = self.get_one(id_element)
            else:
                raise(Exception("Veuillez choisir une option valide"))
        return one_tournament

    def select_one_tournament(self):
        """ function that permits to select an tournament for execution """
        tournaments_view = TournamentView()
        choice, id_tournament = tournaments_view.show_load_create("tournoi")
        one_tournament = self.load_create(choice, id_tournament)
        return one_tournament

    def add_players_tournament(self, one_tournament):
        tournaments_view = TournamentView()
        nber_players = len(one_tournament.list_players)
        if nber_players <= 8:
            nb = 0
            choice = tournaments_view.show_initialize_players()
            if choice == 'U':
                while nb <= 7:
                    choice, id_player = tournaments_view.show_load_create(
                            "joueur"
                        )
                    one_player = PlayerController().load_create(
                        choice, id_player
                        )
                    one_tournament.list_players.append(one_player.identifier)
                    nb = nb+1
            else:
                file = tournaments_view.id_players_file()
                players.load_from_json(file)
                one_tournament.list_players = PlayerController().players_json(file)

    def generate_matchs_firstRound(self, tournament):
        """ function that generates matchs for the 1er Round """
        list_players = tournament.list_players
        all_list_players = []
        for elt in list_players:
            all_list_players.append(PlayerController().get_one(elt))
        list_triee = sorted(
                    all_list_players,
                    key=attrgetter("rank"),
                    reverse=True
                    )
        tournament.matches_dones += [
                f"{list_triee[0].identifier}:{list_triee[4].identifier}",
                f"{list_triee[1].identifier}:{list_triee[5].identifier}",
                f"{list_triee[2].identifier}:{list_triee[6].identifier}",
                f"{list_triee[3].identifier}:{list_triee[7].identifier}"
            ]
        tournament.list_rounds.append(Round("Round 1", [
            Match("Match1", list_triee[0], 0, list_triee[4], 0),
            Match("Match2", list_triee[1], 0, list_triee[5], 0),
            Match("Match3", list_triee[2], 0, list_triee[6], 0),
            Match("Match4", list_triee[3], 0, list_triee[7], 0)
            ], "", ""))
        return tournament

    def enter_scores_round(self, one_tournament):
        """ function thats can enter scores of a round """
        list_rounds = one_tournament.list_rounds
        tournaments_form = TournamentForm()
        tournaments_form.enter_scores(list_rounds[-1])

    def diff_list_matches(self, l1, l2):
        list_diff = list(set(l1) - set(l2))
        return list_diff

    def give_next_match(self, one_player, sorted_list, matches_allowed):
        id_player1 = str(one_player[0].identifier)
        if sorted_list is not None:
            for elt in sorted_list:
                id_player2 = str(elt[0].identifier)
                match_plays = []
                if self.sort_play(id_player1, id_player2) in matches_allowed:
                    match_plays.append(one_player)
                    match_plays.append(elt)
                    return match_plays

    def sort_play(self, p1, p2):
        return f"{min(p1, p2)}:{max(p1, p2)}"

    def matchs_2to4Rounds(self, tournament):
        """
         function thats generates matches of 2 to 4 rounds
        """
        all_list_players = []
        list_triee = []
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
        matches_list = tournament.list_players
        matches_dones = tournament.matches_dones
        matches_comb = [self.sort_play(p1, p2)
                        for p1, p2 in combinations(matches_list, 2)]
        matches_diff = self.diff_list_matches(matches_comb, matches_dones)
        matches_for_next_round = []
        while len(sorted_only_players) > 2:
            elt = sorted_only_players[0]
            res = self.give_next_match(elt, sorted_only_players, matches_diff)
            matches_for_next_round.append(res)
            sorted_only_players.remove(res[0])
            sorted_only_players.remove(res[1])
        matches_for_next_round.append(sorted_only_players)
        all_new_matches = []
        tournament.matches_dones += [
            str(matches_for_next_round[0][0][0].identifier)+":"+str(
                matches_for_next_round[0][1][0].identifier),
            str(matches_for_next_round[1][0][0].identifier)+":"+str(
                matches_for_next_round[1][1][0].identifier),
            str(matches_for_next_round[2][0][0].identifier)+":"+str(
                matches_for_next_round[2][1][0].identifier),
            str(matches_for_next_round[3][0][0].identifier)+":"+str(
                matches_for_next_round[3][1][0].identifier)
        ]
        all_new_matches.append(
            Match(
                "Match1",
                matches_for_next_round[0][0][0],
                matches_for_next_round[0][0][1],
                matches_for_next_round[0][1][0],
                matches_for_next_round[0][1][1]))
        all_new_matches.append(
            Match(
                "Match 2",
                matches_for_next_round[1][0][0],
                matches_for_next_round[1][0][1],
                matches_for_next_round[1][1][0],
                matches_for_next_round[1][1][1]))
        all_new_matches.append(
            Match(
                "Match 3",
                matches_for_next_round[2][0][0],
                matches_for_next_round[2][0][1],
                matches_for_next_round[2][1][0],
                matches_for_next_round[2][1][1]))
        all_new_matches.append(
            Match(
                "Match 4",
                matches_for_next_round[3][0][0],
                matches_for_next_round[3][0][1],
                matches_for_next_round[3][1][0],
                matches_for_next_round[3][1][1]))
        tournament.list_rounds.append(
            Round(
                f"Round {nbre_tours+1}",
                all_new_matches,
                thelast_round.start_date,
                thelast_round.end_date))
        tournaments.save_to_dbase()
        return tournament

    def players_ranking(self, tournament: Tournament) -> list:
        list_players = []
        result = {}
        list_rounds = tournament.list_rounds
        for r in list_rounds:
            list_matches = r.matches_list
            for match in list_matches:
                player1 = match.match["player1"]
                list_players.append(player1)
                player2 = match.match["player2"]
                list_players.append(player2)
        for e in list_players:
            if e[0].identifier not in result:
                result[e[0].identifier] = [e[0], e[1]]
            else:
                result[e[0].identifier] = [
                    e[0], result[e[0].identifier][1] + e[1]
                    ]
        sorted_ranking = sorted(
                    result.values(),
                    key=lambda x: x[1],
                    reverse=True
        )
        return sorted_ranking

    def close_tournament(self, one_tournament: Tournament):
        """ function that closes properly a tournamenet"""
        TournamentView().show_tournament_done(one_tournament)
        scored_ranking = self.players_ranking(one_tournament)
        PlayersView().show_players_ranking(scored_ranking)
