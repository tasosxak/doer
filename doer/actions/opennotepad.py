
import open

class Opennotepad(open.Open):

    def __init__(self):
        open.Open.__init__(self)
        self.act({"notepad":2,"gedit":1}) #To programma pou theleis na anoiksei prepei na einai sto telos
