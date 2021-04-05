import json
from views.playersForm import PlayersForm
from utils.playersFactory import PlayersFactory
from utils.singleton import Singleton
from controllers.controller import Controller


class PlayerController(Controller):

    def create_one_player(self):
        """ function that creates a new player  """
        a_fab = PlayersFactory.getInstance()
        one_player = PlayersForm().createForm_one_player()
        a_fab.addPlayer(one_player)
        return one_player

    def get_one(self, id_player):
        a_fab = PlayersFactory.getInstance()
        one_player = a_fab.get_one_player(id_player)
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
