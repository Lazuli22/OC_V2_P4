
from itertools import combinations
from operator import itemgetter, attrgetter
from utils.player_manager import player_manager as players
from utils.tournament_manager import tournament_manager as tournaments
from models.match import Match
from models.round import Round

tournaments.load_from_json()
one_tournament = tournaments.find_by_id("Tounoi de Paris_Paris_2000-01-01")
#print(one_tournament)
players.load_from_json()
liste_players = players.find_all()
#print(liste_players)


def diff_list_matches(l1, l2):
    list_diff = list(set(l1) - set(l2))
    return list_diff


def give_next_match(one_player, sorted_list, matches_allowed):
    id_player1 = str(one_player[0].identifier)
    #print(id_player1)
    if sorted_list is not None:
        for elt in sorted_list:
            id_player2 = str(elt[0].identifier)
            #print(id_player2)
            match_plays = []
            #print(sorted_list)
            if id_player1+":"+id_player2 in matches_allowed:
                match_plays.append(one_player)
                match_plays.append(elt)
                return match_plays


def score_players_round(tournament):
    all_list_players = []
    list_triee = []
    #players_controller = PlayerController()
    nbre_tours = len(tournament.list_rounds)
    if nbre_tours > 0:
        thelast_round = tournament.list_rounds[-1]
        list_matches = thelast_round.matches_list
        for elt in list_matches:
            #float(elt.match['player1'][1]) += float(elt.match['player1'][1])
            dict_part1 = (
                            elt.match['player1'][0],
                            elt.match['player1'][0].rank,
                            elt.match['player1'][1],           
                )
            all_list_players.append(dict_part1)
            #float(elt.match['player2'][1]) += float(elt.match['player1'][1])
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
    matches_diff = diff_list_matches(matches_comb, matches_dones)
    #print(len(matches_diff))
    matches_for_next_round = []
    while len(sorted_only_players) > 2:
        elt = sorted_only_players[0]
        res = give_next_match(elt, sorted_only_players, matches_diff)
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


score_players_round(one_tournament)
