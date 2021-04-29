import json
import uuid
from operator import attrgetter
from views.playersForm import PlayersForm
from controllers.controller import Controller
from utils.player_manager import player_manager as players


class PlayerController(Controller):

    def create_one_player(self):
        """ function that creates a new player  """
        one_player = PlayersForm().createForm_one_player()
        players.create(**one_player)
        return one_player

    def players_sort(self, one_sort):
        players_list = players.find_all()
        if one_sort == 'C':
            sorted_list = sorted(
                                players_list,
                                key=attrgetter("rank"),
                                reverse=True)
        elif one_sort == 'O':
            sorted_list = sorted(
                        players_list,
                        key=lambda x: (x.firstname, x.lastname)
                        )
        else:
            print("pas d ordre défini")
        return sorted_list
        
    def get_one(self, id_player):
        id_player = uuid.UUID(id_player)
        one_player = players.find_by_id(id_player)
        return one_player

    def load_create(self, choice, id_element):
        if choice == 'C':
            one_player = self.create_one_player()
        elif choice == "R":
            one_player = self.get_one(id_element)
        else:
            raise(Exception("Veuillez choisir une option valide"))
        return one_player

    def reading_players_json(self, nom):
        """
        function that read a json file and 
        produces a list of id players
        """
        id_liste_players = []
        with open(nom) as f:
            data = json.load(f)
        for elt in data:
            id_liste_players.append(
                elt["player"]["identifier"]
            )
        return id_liste_players
  