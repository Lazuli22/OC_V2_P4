import json
from utils.manager import Manager
from models.player import Player


class PlayerManager(Manager):

    def __init__(self):
        super().__init__(Player, key=lambda x: x.identifier)
    
    def load_from_json(self):
        """
        function that loads a json file and
        initializes the players registry
        """
        with open("players_registry.json") as f:
            data = json.load(f)
        for elt in data:
            self.create(**elt)
    
    def load_from_dbase(self):
        data = self.db.all()["players"]
        for elt in data:
            self.create(**elt)
    

    def save_to_json(self):
        """
        function that saves the players registry
        in a json file
        """
        players = list(self.registry.values())
        the_list = []
        with open("players_registry.json", "w") as f:
            for elt in players:
                ps = elt.serialize()
                the_list.append(ps)
            f.write(json.dumps(the_list, indent=3))
        
    def save_to_dbase(self):
        pass

player_manager = PlayerManager()
