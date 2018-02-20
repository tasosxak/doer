
import actions.open
from subprocess import call

class Opennotepad(actions.open.Open):

    def __init__(self):
        actions.open.Open.__init__(self)
        self.act({"notepad":5,"gedit":1}) #To programma pou theleis na anoiksei prepei na einai sto telos

    def doIt(self,tokens):
        print("Opening " + self.programName)
        call([self.programName])
