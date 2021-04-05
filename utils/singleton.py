

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        """ Return the singleton instance """
        if not cls.__instance:
            cls()
        return cls.__instance
