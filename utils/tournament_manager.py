import json
from utils.manager import Manager
from models.tournament import Tournament


class TournamentManager(Manager):

    def __init__(self):
        super().__init__(Tournament, key=lambda x: x.identifier)

    def save_to_json(self):
        """
        function that saves the tournaments registry in a json file
        """
        tournaments = list(self.registry.values())
        list_tournaments = []
        with open("tournaments_registry.json", "w") as f:
            for elt in tournaments:
                res = elt.serialize()
                list_tournaments.append(res)
            f.write(json.dumps(list_tournaments, indent=3))

    def save_to_dbase(self):
        pass
        

    def load_from_json(self):
        """
            function that loads a json file and
            initialize the tournaments registry
        """
        with open("tournaments_registry.json") as f:
            data = json.load(f)
        for elt in data:
            self.create(**elt)
    
    def load_from_dbase(self):
        data = self.db.all()["tournaments"]
        for elt in data:
            self.create(**elt)


tournament_manager = TournamentManager()
