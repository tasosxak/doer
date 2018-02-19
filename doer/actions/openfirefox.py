
import actions.open

class Openfirefox(actions.open.Open):

    def __init__(self):
        actions.open.Open.__init__(self)
        self.act({"browser":1,"firefox":2}) #To programma pou theleis na anoiksei prepei na einai sto telos
