from doer import say
import actions.action

class Welcome(actions.action.Action):

    def __init__(self):
        self.items = {"hello" : 10, "hi" : 3 , "doer" : 1}
        self.username = "user"

    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self,tokens):
        print("Speaking.. ")
        say("Hello " + self.username)
