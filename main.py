from fuzzy.system import Fuzzy
from fuzzy.variables import Variable
from fuzzy.facts import Fact
from fuzzy.operators import Mamdani
from fuzzy.deffuzification import centroid
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
    # temperature = Variable('temperature', temperature_sets)
    
    inputs = {
        'temperature': Variable('temperature', temperature_sets, (0, 7))
    }

    distance_sets = {
        'near': (m.r_func, (1, 2)),
        'halfway': (m.triangular, (2, 3, 4)),
        'far': (m.l_func, (3, 4)),
    }
    # distance = Variable('distance', distance_sets)
    
    outputs = {
        'distance': Variable('distance', distance_sets, (0, 5))
    }

    # facts = [Fact.parse("temperature IS 2.76")]

    rules = [
        "IF temperature IS cold THEN distance IS near",
        "IF temperature IS cool THEN distance IS near",
        "IF temperature IS nominal THEN distance IS halfway",
        "IF temperature IS warm THEN distance IS far",
        "IF temperature IS hot THEN distance IS far",
    ]

    
    inference_system = Fuzzy(inputs, outputs, Mamdani(), rules, centroid)
    
    crisp_output = inference_system.infer([("temperature", 2.76)])
    print(crisp_output)

    exit(0)

if __name__ == "__main__":
    import sys
    if '--debug' in sys.argv:
        test()
    main()

