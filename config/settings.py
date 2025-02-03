# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:05 2025

@author: fajma
"""


functions = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": "(x**2 + y - 11)**2 + (x + y**2 - 7)**2",
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": "(1 - x)**2 + 100 * (y - x**2)**2",
    "Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": "(1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2",
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": "0.26*(x**2 + y**2) - 0.48*x*y",
    "Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": 
        "-20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20",
    "Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": 
        "20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))",
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": "2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2",
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": 
        "(4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2"
    #"... or be creative": None
}

ranges = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": (-5, 5, -5, 5),
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": (-2, 2, -1, 3),
    "Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": (-4.5, 4.5, -4.5, 4.5),
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": (-10, 10, -10, 10),
    "Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": (-5, 5, -5, 5),
    "Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": (-5.12, 5.12, -5.12, 5.12),
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": (-3, 3, -3, 3),
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": (-2, 2, -2, 2)
}

global_minima = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": [((3, 2), 0), ((-2.805, 3.131), 0)],
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": [((1, 1), 0)],
    "Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": [((3, 0.5), 0)],
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": [((0, 0), 0)],
    "Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": [((0, 0), 0)],
    "Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": [((0, 0), 0)],
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": [((0, 0), -1.0316)],
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": [((0, -1.2), -1.0316), ((0.5, 0.5), -0.836)]
}

local_minima = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": [],
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": [],
    "Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": [],
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": [],
    "Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": [],
    "Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": [],
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": [((1.5, -0.5), -0.4627)],
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": [((0.5, 0.5), -0.836), ((-0.5, 0.5), -0.5)]
}

OPTIMIZER_SETTINGS = {
    "SGD": {
        "learning_rate": 0.001,  # Default learning rate
    },
    "Adam": {
        "learning_rate": 0.001,
    },
    "Adagrad": {
        "learning_rate": 0.001,
    },
    "RMSprop": {
        "learning_rate": 0.001,
    }
}
