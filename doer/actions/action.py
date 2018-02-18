# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

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
    def doIt(self):
        pass
