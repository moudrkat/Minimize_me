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

optimizer_descriptions = {
    "SGD": {
        "name": "Stochastic Gradient Descent (SGD)",
        "formula": r"""
        \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \nabla f(\mathbf{w})
        """,
        "momentum_formula": r"""
        v_t = \beta v_{t-1} + \nabla f(\mathbf{w})
        """,
        "update_with_momentum": r"""
        \mathbf{w}_{\text{new}} = \mathbf{w} - \eta v_t
        """,
        "explanation": "Stochastic Gradient Descent (SGD) is a simple optimization algorithm that updates parameters using the gradient of the loss function. Adding momentum helps accelerate SGD in the relevant direction and dampens oscillations. \(\beta\) is the momentum factor, which controls how much of the previous gradient is retained."
    },
    "Adam": {
        "name": "Adam (Adaptive Moment Estimation)",
        "formula": r"""
        m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla f(\mathbf{w})
        """,
        "additional_formula": r"""
        v_t = \beta_2 v_{t-1} + (1 - \beta_2) \nabla f(\mathbf{w})^2
        """,
        "corrected_moment": r"""
        \hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
        """,
        "final_update": r"""
        \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
        """,
        "explanation": "Adam combines ideas from both Momentum and RMSprop. It uses exponentially decaying averages of past gradients and squared gradients. \(\beta_1\) and \(\beta_2\) are decay rates for the moment estimates, and \(\epsilon\) is a small constant to prevent division by zero."
    },
    "Adagrad": {
        "name": "Adagrad",
        "formula": r"""
        \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{G_t} + \epsilon} \nabla f(\mathbf{w})
        """,
        "explanation": "Adagrad adjusts the learning rate for each parameter based on the sum of the squared gradients. It is especially useful for sparse data or features."
    },
    "RMSprop": {
        "name": "RMSprop",
        "formula": r"""
        \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{v_t + \epsilon}} \nabla f(\mathbf{w})
        """,
        "explanation": "RMSprop modifies Adagrad by introducing a moving average of squared gradients, helping to avoid the rapid decrease in the learning rate. It works well for non-stationary objectives."
    }
}

OPTIMIZER_SETTINGS = {
    "SGD": {
         "learning_rate": 0.01,
         "momentum": 0.0,
        # "nesterov": True,
        # "weight_decay": 0.0001,  
        # "clipvalue": 0.5  
    },
    "Adam": {
         "learning_rate": 0.001
    },
    "RMSprop": {
         "learning_rate": 0.001

    },
    "Adagrad": {
         "learning_rate": 0.01
    }
}
