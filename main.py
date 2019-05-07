from fuzzy.system import Fuzzy
from fuzzy.variables import Variable
from fuzzy.facts import Fact
from fuzzy.operators import Default
from fuzzy.defuzzification import *
from fuzzy.aggregations import *
from fuzzy.utils import plot
from fuzzy import membership as m
from functools import partial

def main():
    pass

def test():
    temp_domain = (0, 7)
    temperature_sets = {
        'cold': (m.r_func, (1, 2)),
        'cool': (m.triangular, (1, 2, 3)),
        'nominal': (m.trapezoidal, (2, 3, 4, 5)),
        'warm': (m.triangular, (4, 5, 6)),
        'hot': (m.l_func, (5, 6)),
    }
    # temperature = Variable('temperature', temperature_sets)
    
    # fns = []
    # for fn, args in temperature_sets.values():
    #     fns.append(partial(fn, *args))

    # plot(fns, temp_domain)

    inputs = {
        'temperature': Variable('temperature', temperature_sets, temp_domain)
    }

    distance_domain = (0, 5)
    distance_sets = {
        'near': (m.r_func, (1, 2)),
        'halfway': (m.triangular, (2, 3, 4)),
        'far': (m.l_func, (3, 4)),
    }
    # distance = Variable('distance', distance_sets)
    
    # fns = []
    # for fn, args in distance_sets.values():
    #     fns.append(partial(fn, *args))

    # plot(fns, distance_domain)

    outputs = {
        'distance': Variable('distance', distance_sets, distance_domain)
    }

    # facts = [Fact.parse("temperature IS 2.76")]

    rules = [
        "IF temperature IS cold THEN distance IS near",
        "IF temperature IS cool THEN distance IS near",
        "IF temperature IS nominal THEN distance IS halfway",
        "IF temperature IS warm THEN distance IS far",
        "IF NOT temperature IS cool THEN distance IS far",
    ]

    
    # inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, centroid)
    # crisp_output = inference_system.infer([("temperature", 2.76)])
    # print(crisp_output)

    # inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, meanofmaximum)
    # crisp_output = inference_system.infer([("temperature", 2.76)])
    # print(crisp_output)

    # inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, smallestofmaximum)
    # crisp_output = inference_system.infer([("temperature", 2.76)])
    # print(crisp_output)

    # inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, largestofmaximum)
    # crisp_output = inference_system.infer([("temperature", 2.76)])
    # print(crisp_output)

    inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, bisector)
    crisp_output = inference_system.infer([("temperature", 2.76)])
    print(crisp_output)

    exit(0)

if __name__ == "__main__":
    import sys
    if '--debug' in sys.argv:
        test()
    main()

