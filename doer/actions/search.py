import actions.action
from abc import abstractmethod
from subprocess import call
import webbrowser

class Search (actions.action.Action):

    def __init__(self,site):
        self.items = {"search": 9, "look": 2, "find" : 3}
        self.site = site

    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self,tokens):
        link = self.site + "+".join(tokens)
        print("Looking for ... " + link)
        webbrowser.open(link)

    def act(self, items):
        self.items.update(items)
        print(self.items.keys())
