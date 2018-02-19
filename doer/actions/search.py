import action
from abc import abstractmethod
from subprocess import call
from collections import OrderedDict
import webbrowser

class Search (action.Action):

    def __init__(self,site):
        self.items = OrderedDict([("search" , 9), ("look" , 2), ("find" , 3)])
        self.site = site

    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self,tokens):
        link = self.site + "+".join(tokens)
        print "Looking for ... " + link
        webbrowser.open(link)

    def act(self, items):
        self.items.update(items)
        print self.items.keys()
