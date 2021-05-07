from utils.manager import Manager
from models.tournament import Tournament


class TournamentManager(Manager):
    """
    Class that permits to create a tournaments registry.
    Several functions are proposed to manipulate tournaments
    """

    def __init__(self):
        super().__init__(Tournament, key=lambda x: x.identifier)
        self.tournaments_table = self.db.table("tournaments")

    def save_to_dbase(self):
        """
        function that saves all tournaments of the tournaments registry
        """
        self.tournaments_table.truncate()
        tournaments = list(self.registry.values())
        the_list = [elt.serialize() for elt in tournaments]
        self.tournaments_table.insert_multiple(the_list)

    def load_from_dbase(self):
        """
        function that loads all tournaments from db.json
        """
        data = self.tournaments_table.all()
        for elt in data:
            self.create(**elt)


tournament_manager = TournamentManager()
