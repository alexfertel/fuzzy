from fuzzy.system import Fuzzy
from fuzzy.fuzzification import Variable
from fuzzy.facts import Fact
from fuzzy.operators import Mamdani
from fuzzy import membership as m

def main():
    pass

def test():
    temperature_sets = {
        'cold': (m.r_func, (1, 2)),
        'cool': (m.triangular, (1, 2, 3)),
        'nominal': (m.trapezoidal, (2, 3, 4, 5)),
        'warm': (m.triangular, (4, 5, 6)),
        'hot': (m.l_func, (5, 6)),
    }
    temperature = Variable('temperature', temperature_sets)
    
    distance_sets = {
        'near': (m.r_func, (1, 2)),
        'middleway': (m.triangular, (2, 3, 4)),
        'far': (m.l_func, (3, 4)),
    }
    distance = Variable('distance', distance_sets)
    
    facts = [Fact.parse("temperature IS 2.76")]
    Fuzzy([temperature], [distance], facts, Mamdani())
    
    exit(0)

if __name__ == "__main__":
    import sys
    if '--debug' in sys.argv:
        test()
    main()

