from operator import attrgetter
from utils.tournamentsFactory import TournamentsFactory
from views.tournamentsView import TournamentsView
from views.tournamentsForm import TournamentsForm
from utils.singleton import Singleton
from controllers.controller import Controller
from controllers.playerController import PlayerController
from models.match import Match
from models.round import Round


class TournamentController(Controller):

    def create_one_tournement(self):
        """ function that creates a new tournement """
        a_fac = TournamentsFactory.getInstance()
        form = TournamentsForm()
        one_tournament = form.createForm_one_tournament()
        a_fac.addTournament(one_tournament)
        return one_tournament

    def get_one(self, id_tournament):
        """ function that gets a specific Tournament """
        a_fac = TournamentsFactory.getInstance()
        one_tournament = a_fac.get_one_tournement(id_tournament)
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

    def generate_matchs_firstRound(self, tournament):
        """ function that generates matchs for the 1er Round """
        list_players = tournament.list_players
        all_list_players = []
        players_controller = PlayerController.getInstance()
        for elt in list_players:
            all_list_players.append(players_controller.get_one(elt))
        
        list_triee = sorted(
                    all_list_players,
                    key=attrgetter("rank"),
                    reverse=True
                    )
        tournament.list_rounds.append(Round("Round 1", [
            Match("Match1", list_triee[0], 0, list_triee[4], 0),
            Match("Match2", list_triee[1], 0, list_triee[5], 0),
            Match("Match3", list_triee[2], 0, list_triee[6], 0),
            Match("Match4", list_triee[3], 0, list_triee[7], 0)
            ]))
        return tournament














