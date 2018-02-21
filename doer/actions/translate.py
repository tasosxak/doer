from googletrans import Translator
from doer import say
import actions
class Translate (actions.action.Action):

    def __init__(self):
        self.translator = Translator()
        self.items = {"translate" : 10}

    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self,tokens):
        if len(tokens)>1:
            print("Translating " + tokens[0])
            translated_sequence = self.translator.translate(" ".join(tokens), dest='greek')
            print(translated_sequence.text)
            say(translated_sequence.text,lang = "greek")
    def act(self, items):
        self.items.update(items)
        print(self.items.keys())
        self.programName = list(self.items.keys())[-1] #slow
