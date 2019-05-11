from functools import partial
from fuzzy import membership

class Variable:
    def __init__(self, name, sets):
        self.name = name
        self.fuzzy_sets = [partial(membership.__dict__[vname], *args) for vname, args in sets]
    
    def fuzzify(self, value):
        return tuple([fn(value) for fn in self.fuzzy_sets])

    def __eq__(self, other):
        return self.name == other.name