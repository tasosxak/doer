
from abc import ABCMeta, abstractmethod

class Action:

    __metaclass__ = ABCMeta

    @abstractmethod
    def getWords(self):
        pass

    @abstractmethod
    def getPoints(self):
        pass

    @abstractmethod
    def doIt(self,tokens):
        pass
