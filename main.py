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
        'none': (m.gaussian, (0, 35)),
        'light': (m.gaussian, (32.5, 13)),
        'moderate': (m.gaussian, (50, 20)),
        'superior': (m.gaussian, (67.5, 13)),
        'complete': (m.gaussian, (100, 25)),
    }

    # fns = []
    # for label, (fn, args) in map_control_sets.items():
    #     fns.append((partial(fn, *args), label))
    # plot_with_labels(fns, map_control_domain)

    gold_lead_domain = (-100, 100)
    gold_lead_sets = {
        'losing by far': (m.gaussian, (-100, 40)),
        'losing': (m.gaussian, (-50, 35)),
        'losing by a little': (m.gaussian, (-25, 25)),
        'leverage': (m.gaussian, (0, 10)),
        'winning by a little': (m.gaussian, (25, 25)),
        'winning': (m.gaussian, (50, 35)),
        'winning by far': (m.gaussian, (100, 15)),
    }

    inputs = {
        'map control': Variable('map control', map_control_sets, map_control_domain),
        'gold lead': Variable('gold lead', gold_lead_sets, gold_lead_domain)
    }

    show_hero_domain = (0, 100)
    show_hero_sets = {
        'never': (m.gaussian, (0, 30)),
        'a little': (m.gaussian, (30, 15)),
        'moderately': (m.gaussian, (55, 25)),
        'a while': (m.gaussian, (80, 12.5)),
        'always': (m.gaussian, (100, 2)),
    }

    # fns = []
    # for label, (fn, args) in map_control_sets.items():
    #     fns.append((partial(fn, *args), label.split(' ')[-1]))
    # plot_with_labels(fns, map_control_domain)
    # fns = []
    # for label, (fn, args) in gold_lead_sets.items():
    #     fns.append((partial(fn, *args), label.split(' ')[-1]))
    # plot_with_labels(fns, gold_lead_domain)
    # fns = []
    # for label, (fn, args) in show_hero_sets.items():
    #     fns.append((partial(fn, *args), label.split(' ')[-1]))
    # plot_with_labels(fns, show_hero_domain)

    outputs = {
        'show hero': Variable('show hero', show_hero_sets, show_hero_domain)
    }

    # rules = [
    #     "IF map control IS close AND gold lead IS very slow THEN show hero IS light",
    #     "IF map control IS close AND gold lead IS slow THEN show hero IS moderate",
    #     "IF map control IS close AND gold lead IS moderate THEN show hero IS hard",
    #     "IF map control IS close AND ( gold lead IS fast OR gold lead IS very fast ) THEN show hero IS hard",

    #     "IF map control IS medium AND ( gold lead IS very slow OR gold lead IS slow ) THEN show hero IS light",
    #     "IF map control IS medium AND ( gold lead IS moderate OR gold lead IS fast ) THEN show hero IS moderate",
    #     "IF map control IS medium AND gold lead IS very fast THEN show hero IS hard",

    #     "IF map control IS far AND ( gold lead IS slow OR gold lead IS moderate OR gold lead IS very slow ) THEN show hero IS light",
    #     "IF map control IS far AND ( gold lead IS fast OR gold lead IS very fast ) THEN show hero IS moderate",
    # ]


    rules = [
        "IF map control IS none AND gold lead IS losing by far THEN show hero IS never",
        "IF map control IS none AND gold lead IS losing THEN show hero IS never",
        "IF map control IS none AND gold lead IS losing by a little THEN show hero IS a little",
        "IF map control IS none AND gold lead IS leverage THEN show hero IS a little",
        "IF map control IS none AND gold lead IS winning by a little THEN show hero IS moderately",
        "IF map control IS none AND gold lead IS winning THEN show hero IS moderately",
        "IF map control IS none AND gold lead IS winning by far THEN show hero IS a while",

        "IF map control IS light AND gold lead IS losing by far THEN show hero IS never",
        "IF map control IS light AND gold lead IS losing THEN show hero IS a little",
        "IF map control IS light AND gold lead IS losing by a little THEN show hero IS a little",
        "IF map control IS light AND gold lead IS leverage THEN show hero IS moderately",
        "IF map control IS light AND gold lead IS winning by a little THEN show hero IS moderately",
        "IF map control IS light AND gold lead IS winning THEN show hero IS a while",
        "IF map control IS light AND gold lead IS winning by far THEN show hero IS a while",

        "IF map control IS moderate AND gold lead IS losing by far THEN show hero IS a little",
        "IF map control IS moderate AND gold lead IS losing THEN show hero IS a little",
        "IF map control IS moderate AND gold lead IS losing by a little THEN show hero IS moderately",
        "IF map control IS moderate AND gold lead IS leverage THEN show hero IS a while",
        "IF map control IS moderate AND gold lead IS winning by a little THEN show hero IS a while",
        "IF map control IS moderate AND gold lead IS winning THEN show hero IS a while",
        "IF map control IS moderate AND gold lead IS winning by far THEN show hero IS always",

        "IF map control IS superior AND gold lead IS losing by far THEN show hero IS moderately",
        "IF map control IS superior AND gold lead IS losing THEN show hero IS moderately",
        "IF map control IS superior AND gold lead IS losing by a little THEN show hero IS moderately",
        "IF map control IS superior AND gold lead IS leverage THEN show hero IS a while",
        "IF map control IS superior AND gold lead IS winning by a little THEN show hero IS always",
        "IF map control IS superior AND gold lead IS winning THEN show hero IS always",
        "IF map control IS superior AND gold lead IS winning by far THEN show hero IS always",

        "IF map control IS complete AND gold lead IS losing by far THEN show hero IS a little",
        "IF map control IS complete AND gold lead IS losing THEN show hero IS moderately",
        "IF map control IS complete AND gold lead IS losing by a little THEN show hero IS a while",
        "IF map control IS complete AND gold lead IS leverage THEN show hero IS a while",
        "IF map control IS complete AND gold lead IS winning by a little THEN show hero IS always",
        "IF map control IS complete AND gold lead IS winning THEN show hero IS always",
        "IF map control IS complete AND gold lead IS winning by far THEN show hero IS always",
    ]

    inference_system = Fuzzy(inputs, outputs, Default(), rules, truncate, bisector)
    # crisp_output = inference_system.infer([("map control", 33.43), ("gold lead", 15)])
    # print(crisp_output)

    n = 100
    s = 20
    xa, xb = map_control_domain
    x_val = [x for x in np.arange(xa, xb, (xb - xa) / n) for _ in range(s)]
   
    ya, yb = gold_lead_domain   
    y_val = [y for y in np.arange(ya, yb, (yb - ya) / n)] * s
    z_val = [inference_system.infer([("map control", x_val[i]), ("gold lead", y_val[i])])["show hero"] for i in range(len(x_val))]

    for x, y, z in zip(x_val, y_val, z_val):
        print(x, y, z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(s):
        c = colors[i % len(colors)]
        for x, y, z in zip(x_val[i * n: i * n + n], y_val[i * n: i * n + n], z_val[i * n: i * n + n]):
            ax.scatter(x, y, z, c=c)
            
    ax.set_xlabel('Control del mapa')
    ax.set_ylabel('Ventaja en oro')
    ax.set_zlabel('Mostrar el héroe')

    # plt.savefig(f'paper/images/{name}.png', bbox_inches='superior')
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

