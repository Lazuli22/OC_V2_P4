import abc


class Factory(metaclass=abc.ABCMeta):
    """
    abstract class that creates element of a tounament
    """
    @abc.abstractclassmethod
    def create(self, dict_data):
        """
        abstract method that creates a tournament or a player
        with a dict of data.
        """
        pass
