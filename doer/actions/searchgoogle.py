
import search
from collections import OrderedDict

class Searchgoogle(search.Search):

    def __init__(self):
        search.Search.__init__(self, "https://www.google.gr/search?q=")
        self.act(OrderedDict([("google",4)]))
