from utils.manager import Manager
from models.player import Player


class PlayerManager(Manager):
    """
    Class that permits to create a players registry
    """
    def __init__(self):
        super().__init__(Player, key=lambda x: x.identifier)
        self.table_players = self.db.table("players")

    def load_from_dbase(self):
        """  function that  loads all players from db.json """
        data = self.table_players.all()
        for elt in data:
            self.create(**elt)

    def save_to_dbase(self):
        """ function that stores all players of the registry players"""
        self.table_players.truncate()
        players = list(self.registry.values())
        the_list = [elt.serialize() for elt in players]
        self.table_players.insert_multiple(the_list)


player_manager = PlayerManager()
