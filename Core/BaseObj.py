class BaseObj:
    def __init__(self):
        pass

    @staticmethod
    def table():
        """
        Return Data Base Table Name
        :return: String
        """
        raise NotImplementedError

    @staticmethod
    def insertKeys():
        """
        Return A list Include All Necessary Insert Key
        :return: List
        """
        raise NotImplementedError

    @staticmethod
    def updateKeys():
        """
        Return A list Include All Necessary Update Key
        :return: List
        """
        raise NotImplementedError

    @staticmethod
    def searchKeys():
        """
        Return A list Include All Necessary Search Key
        :return: List
        """
        raise NotImplementedError
