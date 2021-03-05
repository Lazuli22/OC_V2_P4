import abc


class Serializable(abc.ABC):

    @abc.abstractclassmethod
    def serialize(self):
        pass



