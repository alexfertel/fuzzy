from functools import partial
from fuzzy import membership

class Variable:
    def __init__(self, name, sets, domain):
        self.name = name
        self.sets = sets
        self.domain = domain
        # print(sets.items())
        self.fuzzy_sets = { sname: partial(fn, *args) for sname, (fn, args) in sets.items() }
    
    def fuzzify(self, value):
        return { sname: fn(value) for sname, fn in self.fuzzy_sets.items() }

    def __eq__(self, other):
        return self.name == other.name


