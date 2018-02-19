
import actions.open
from collections import OrderedDict

class Opennotepad(actions.open.Open):

    def __init__(self):
        actions.open.Open.__init__(self)
        self.act(OrderedDict([("notepad",2),("gedit",1)])) #To programma pou theleis na anoiksei prepei na einai sto telos
