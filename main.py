from fuzzy.system import Fuzzy
from fuzzy.variables import Variable
from fuzzy.facts import Fact
from fuzzy.operators import Default
from fuzzy.defuzzification import *
from fuzzy.aggregations import *
from fuzzy.utils import plot, compose
from fuzzy import membership as m
from functools import partial

def main():
    distance_to_stop_domain = (0, 100)
    distance_to_stop_sets = {
        'close': (m.r_func, (25, 30)),
        'medium': (m.trapezoidal, (15, 30, 55, 65)),
        'far': (m.l_func, (55, 70)),
    }


    speed_domain = (0, 140)
    speed_sets = {
        'very slow': (m.r_func, (15, 20)),
        'slow': (m.trapezoidal, (17, 25, 45, 50)),
        'medium': (m.trapezoidal, (45, 55, 65, 75)),
        'fast': (m.triangular, (65, 100, 125)),
        'very fast': (m.l_func, (110, 120)),
    }


    inputs = {
        'distance to stop': Variable('distance to stop', distance_to_stop_sets, distance_to_stop_domain),
        'speed': Variable('speed', speed_sets, speed_domain)
    }

    break_pressure_domain = (0, 100)
    break_pressure_sets = {
        'light': (m.r_func, (2, 10)),
        'moderate': (m.triangular, (8, 40, 62)),
        'hard': (m.l_func, (55, 95)),
    }

    # fns = []
    # for fn, args in distance_to_stop_sets.values():
    #     fns.append(partial(fn, *args))
    # plot(fns, distance_to_stop_domain)
    # fns = []
    # for fn, args in speed_sets.values():
    #     fns.append(partial(fn, *args))
    # plot(fns, speed_domain)
    # fns = []
    # for fn, args in break_pressure_sets.values():
    #     fns.append(partial(fn, *args))
    # plot(fns, break_pressure_domain)

    outputs = {
        'break pressure': Variable('break pressure', break_pressure_sets, break_pressure_domain)
    }

    rules = [
        "IF distance to stop IS close AND speed IS very slow THEN break pressure IS light",
        "IF distance to stop IS close AND speed IS slow THEN break pressure IS moderate",
        "IF distance to stop IS close AND speed IS medium THEN break pressure IS hard",
        "IF distance to stop IS close AND ( speed IS fast OR speed IS very fast ) THEN break pressure IS hard",

        "IF distance to stop IS medium AND ( speed IS very slow OR speed IS slow ) THEN break pressure IS light",
        "IF distance to stop IS medium AND ( speed IS medium OR speed IS fast ) THEN break pressure IS moderate",
        "IF distance to stop IS medium AND speed IS very fast THEN break pressure IS hard",

        "IF distance to stop IS far AND ( speed IS slow OR speed IS medium OR speed IS very slow ) THEN break pressure IS light",
        "IF distance to stop IS far AND ( speed IS fast OR speed IS very fast ) THEN break pressure IS moderate",
    ]

    # rules = [
    #     "IF distance to stop IS close AND speed IS very slow THEN break pressure IS light",
    #     "IF distance to stop IS close AND speed IS slow THEN break pressure IS moderate",
    #     "IF distance to stop IS close AND speed IS medium THEN break pressure IS hard",
    #     "IF distance to stop IS close AND speed IS fast THEN break pressure IS hard",
    #     "IF distance to stop IS close AND speed IS very fast THEN break pressure IS hard",

    #     "IF distance to stop IS medium AND speed IS very slow THEN break pressure IS light",
    #     "IF distance to stop IS medium AND speed IS slow THEN break pressure IS light",
    #     "IF distance to stop IS medium AND speed IS medium THEN break pressure IS moderate",
    #     "IF distance to stop IS medium AND speed IS fast THEN break pressure IS moderate",
    #     "IF distance to stop IS medium AND speed IS very fast THEN break pressure IS hard",

    #     "IF distance to stop IS far AND speed IS very slow THEN break pressure IS light",
    #     "IF distance to stop IS far AND speed IS slow THEN break pressure IS light",
    #     "IF distance to stop IS far AND speed IS medium THEN break pressure IS light",
    #     "IF distance to stop IS far AND speed IS fast THEN break pressure IS moderate",
    #     "IF distance to stop IS far AND speed IS very fast THEN break pressure IS moderate",
    # ]

    inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, centroid)
    crisp_output = inference_system.infer([("distance to stop", 33.43), ("speed", 140)])
    print(crisp_output)


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

