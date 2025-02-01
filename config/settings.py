# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:05 2025

@author: fajma
"""

# Function dictionary
functions = {
    #"Sphere: x**2 + y**2": "x**2 + y**2",
    #"Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": "(1 - x)**2 + 100 * (y - x**2)**2",
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": "(x**2 + y - 11)**2 + (x + y**2 - 7)**2",
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2":"2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2",
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y" : "0.26*(x**2 + y**2) - 0.48*x*y",
    "... or be creative": None,
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
