import uuid
import json
from operator import attrgetter
from views.player_form import PlayerForm
from controllers.controller import Controller
from utils.player_manager import player_manager as players


class PlayerController(Controller):

    def create_one(self):
        """ function that creates a new player  """
        one_player = PlayerForm().createForm_one_player()
        return players.create(**one_player)

    def modify_one_player(self, id_player):
        """  function that modifies a player rank"""
        one_player = self.get_one(id_player)
        PlayerForm().modifyForm_one_player(one_player)
        return one_player

    def get_one(self, id_player):
        """ function that finds a player with its identifier"""
        id_player = uuid.UUID(id_player)
        one_player = players.find_by_id(id_player)
        return one_player

    def players_sort(self, one_sort, one_tournament):
        """ function that shows a sorted list players """
        players_list = []
        if one_tournament is None:
            players_list = players.find_all()
        else:
            for elt in one_tournament.list_players:
                id_player = uuid.UUID(elt)
                players_list.append(players.find_by_id(id_player))
        if one_sort == 'C':
            sorted_list = sorted(
                                players_list,
                                key=attrgetter("rank"),
                                reverse=True)
        elif one_sort == 'O':
            sorted_list = sorted(
                        players_list,
                        key=lambda x: (x.lastname, x.firstname)
                        )
        else:
            print("pas d ordre défini")
        return sorted_list

    def load_create(self, choice, id_element):
        """ Function that gives the choix to load or create a player """
        if choice == 'C':
            one_player = self.create_one()
        elif choice == "R":
            one_player = self.get_one(id_element)
        else:
            raise(Exception("Veuillez choisir une option valide"))
        return one_player

    def players_json(self, nom):
        """
        function that read a json file and
        produces a list of id players
        """
        id_liste_players = []
        with open(nom) as f:
            data = json.load(f)
        for elt in data:
            id_liste_players.append(
                elt["identifier"]
            )
        return id_liste_players
