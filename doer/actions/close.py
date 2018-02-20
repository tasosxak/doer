import actions.action
from abc import abstractmethod
from subprocess import Popen


class Close (actions.action.Action):

    def __init__(self):
        self.items = {"close" : 10, "program" : 3 , "app" : 1 , "application" : 1}
        self.programName = ""


    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self,tokens):
        print("Closing " + tokens[0])
        try:
            Popen(["pkill","-f",tokens[0]])
        except:
            print("The program " + tokens[0] + "doesn't exists :/")

    def act(self, items):
        self.items.update(items)
        print(self.items.keys())
        self.programName = list(self.items.keys())[-1] #slow
