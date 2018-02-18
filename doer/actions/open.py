import action
from abc import abstractmethod
from subprocess import call
from collections import OrderedDict

class Open (action.Action):

    def __init__(self):
        self.items = OrderedDict([("open" , 10), ("program" , 5), ("app" , 1),("application" , 1)])
        self.programName = ""


    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self):
        print "Opening " + self.programName
        call([self.programName])

    def act(self, items):
        self.items.update(items)
        print self.items.keys()
        self.programName = self.items.keys()[-1]
