import actions.search

class Searchgoogle(actions.search.Search):

    def __init__(self):
        actions.search.Search.__init__(self, "https://www.google.gr/search?q=")
        self.act({"google":4})
