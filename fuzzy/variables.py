from functools import partial
from fuzzy import membership

class Variable:
    def __init__(self, name, sets):
        self.name = name
        self.sets = sets
        self.fuzzy_sets = { partial(membership.__dict__[vname], *args) for vname, args in sets}
    
    def fuzzify(self, value):
        return tuple([fn(value) for _, fn in self.sets])

    def __eq__(self, other):
        return self.name == other.name


