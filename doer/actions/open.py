
import actions.action
from abc import abstractmethod
from subprocess import call


class Open (actions.action.Action):

    def __init__(self):
        self.items = {"open" : 10, "program" : 3 , "app" : 1 , "application" : 1}
        self.programName = ""


    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self,tokens):
        print("Opening " + tokens[0])
        try:
            call([tokens[0]])
        except:
            print("The program " + tokens[0] + "doesn't exist :/")

    def act(self, items):
        self.items.update(items)
        print(self.items.keys())
        self.programName = list(self.items.keys())[-1] #slow
