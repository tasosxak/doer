
import open
from collections import OrderedDict
class Openfirefox(open.Open):

    def __init__(self):
        open.Open.__init__(self)
        self.act(OrderedDict([("browser",1),("firefox",2)])) #To programma pou theleis na anoiksei prepei na einai sto telos
