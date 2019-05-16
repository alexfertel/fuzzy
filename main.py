from fuzzy.system import Fuzzy
from fuzzy.variables import Variable
from fuzzy.operators import Default
from fuzzy.defuzzification import *
from fuzzy.aggregations import *
from fuzzy.utils import plot, plot_with_labels, compose
from fuzzy import membership as m
from functools import partial

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def main():
    map_control_domain = (0, 100)
    map_control_sets = {
        'none': (m.r_func, (15, 35)),
        'light': (m.gaussian, (32.5, 13)),
        'moderate': (m.gaussian, (50, 20)),
        'tight': (m.gaussian, (67.5, 13)),
        'complete': (m.l_func, (55, 75)),
    }

    fns = []
    for label, (fn, args) in map_control_sets.items():
        fns.append((partial(fn, *args), label))
    plot_with_labels(fns, map_control_domain)

    speed_domain = (0, 140)
    speed_sets = {
        'very slow': (m.r_func, (15, 20)),
        'slow': (m.triangular, (7, 30, 50)),
        'moderate': (m.triangular, (35, 60, 85)),
        'fast': (m.triangular, (55, 100, 130)),
        'very fast': (m.l_func, (90, 120)),
    }


    inputs = {
        'distance to stop': Variable('distance to stop', map_control_sets, map_control_domain),
        'speed': Variable('speed', speed_sets, speed_domain)
    }

    break_pressure_domain = (0, 100)
    break_pressure_sets = {
        'light': (m.r_func, (2, 25)),
        'moderate': (m.triangular, (4, 40, 75)),
        'hard': (m.l_func, (43, 95)),
    }

    # fns = []
    # for label, (fn, args) in map_control_sets.items():
    #     fns.append((partial(fn, *args), label))
    # plot_with_labels(fns, map_control_domain)
    # fns = []
    # for label, (fn, args) in speed_sets.items():
    #     fns.append((partial(fn, *args), label))
    # plot_with_labels(fns, speed_domain)
    # fns = []
    # for label, (fn, args) in break_pressure_sets.items():
    #     fns.append((partial(fn, *args), label))
    # plot_with_labels(fns, break_pressure_domain)

    outputs = {
        'break pressure': Variable('break pressure', break_pressure_sets, break_pressure_domain)
    }

    # rules = [
    #     "IF distance to stop IS close AND speed IS very slow THEN break pressure IS light",
    #     "IF distance to stop IS close AND speed IS slow THEN break pressure IS moderate",
    #     "IF distance to stop IS close AND speed IS moderate THEN break pressure IS hard",
    #     "IF distance to stop IS close AND ( speed IS fast OR speed IS very fast ) THEN break pressure IS hard",

    #     "IF distance to stop IS medium AND ( speed IS very slow OR speed IS slow ) THEN break pressure IS light",
    #     "IF distance to stop IS medium AND ( speed IS moderate OR speed IS fast ) THEN break pressure IS moderate",
    #     "IF distance to stop IS medium AND speed IS very fast THEN break pressure IS hard",

    #     "IF distance to stop IS far AND ( speed IS slow OR speed IS moderate OR speed IS very slow ) THEN break pressure IS light",
    #     "IF distance to stop IS far AND ( speed IS fast OR speed IS very fast ) THEN break pressure IS moderate",
    # ]

    rules = [
        "IF distance to stop IS close AND speed IS very slow THEN break pressure IS light",
        "IF distance to stop IS close AND speed IS slow THEN break pressure IS moderate",
        "IF distance to stop IS close AND speed IS moderate THEN break pressure IS hard",
        "IF distance to stop IS close AND speed IS fast THEN break pressure IS hard",
        "IF distance to stop IS close AND speed IS very fast THEN break pressure IS hard",

        "IF distance to stop IS medium AND speed IS very slow THEN break pressure IS light",
        "IF distance to stop IS medium AND speed IS slow THEN break pressure IS light",
        "IF distance to stop IS medium AND speed IS moderate THEN break pressure IS moderate",
        "IF distance to stop IS medium AND speed IS fast THEN break pressure IS moderate",
        "IF distance to stop IS medium AND speed IS very fast THEN break pressure IS hard",

        "IF distance to stop IS far AND speed IS very slow THEN break pressure IS light",
        "IF distance to stop IS far AND speed IS slow THEN break pressure IS light",
        "IF distance to stop IS far AND speed IS moderate THEN break pressure IS light",
        "IF distance to stop IS far AND speed IS fast THEN break pressure IS moderate",
        "IF distance to stop IS far AND speed IS very fast THEN break pressure IS moderate",
    ]

    inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, smallestofmaximum)
    # crisp_output = inference_system.infer([("distance to stop", 33.43), ("speed", 140)])
    # print(crisp_output)

    n = 100
    xa, xb = map_control_domain
    x_val = [x for x in np.arange(xa, xb, (xb - xa) / n) for _ in range(10)]
   
    ya, yb = speed_domain   
    y_val = [y for y in np.arange(ya, yb, (yb - ya) / n)] * 10
    z_val = [inference_system.infer([("distance to stop", x_val[i]), ("speed", y_val[i])])["break pressure"] for i in range(len(x_val))]

    for x, y, z in zip(x_val, y_val, z_val):
        print(x, y, z)

    ax = plt.axes(projection='3d')
    ax.scatter3D(x_val, y_val, z_val)

    ax.set_xlabel('Distancia al pare')
    ax.set_ylabel('Velocidad')
    ax.set_zlabel('Presión aplicada')

    # plt.savefig(f'paper/images/{name}.png', bbox_inches='tight')
    plt.show()




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

