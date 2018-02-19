
import actions.search
from collections import OrderedDict

class Searchgoogle(actions.search.Search):

    def __init__(self):
        actions.search.Search.__init__(self, "https://www.google.gr/search?q=")
        self.act(OrderedDict([("google",4)]))
