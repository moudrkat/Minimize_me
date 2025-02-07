# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:05 2025

@author: fajma
"""

# Function formulas (Python)
FORMULAS = {
    "Himmelblau": "(x**2 + y - 11)**2 + (x + y**2 - 7)**2",
    "Rosenbrock": "(1 - x)**2 + 100 * (y - x**2)**2",
    "Matyas": "0.26*(x**2 + y**2) - 0.48*x*y",
    "Three-hump Camel": "2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2",
    "Six-hump Camel": "(4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2"
}

# LaTeX formatted formulas
LATEX_FORMULAS = {
    "Himmelblau": r"$(x^2 + y - 11)^2 + (x + y^2 - 7)^2$",
    "Rosenbrock": r"$(1 - x)^2 + 100 \cdot (y - x^2)^2$",
    "Matyas": r"$0.26(x^2 + y^2) - 0.48xy$",
    "Three-hump Camel": r"$2x^2 - 1.05x^4 + \frac{x^6}{6} + xy + y^2$",
    "Six-hump Camel": r"$(4 - 2.1x^2 + \frac{x^4}{3}) x^2 + xy + (-4 + 4y^2) y^2$"
}

# Ranges
RANGES = {
    "Himmelblau": (-5, 5, -5, 5),
    "Rosenbrock": (-2, 2, -1, 3),
    "Matyas": (-10, 10, -10, 10),
    "Three-hump Camel": (-2, 2, -1.5, 1.5),
    "Six-hump Camel": (-2, 2, -1, 1)
}

# Global minima
GLOBAL_MINIMA = {
    "Himmelblau": [((3, 2), 0), ((-2.805, 3.131), 0), ((-3.779, -3.283), 0), ((3.584, -1.848), 0)],
    "Rosenbrock": [((1, 1), 0)],
    "Matyas": [((0, 0), 0)],
    "Three-hump Camel": [((0, 0), -1.0316)],
    "Six-hump Camel": [((0.0898, -0.7126), -1.0316), ((-0.0898, 0.7126), -1.0316)]
}

optimizer_descriptions = {
    "SGD": {
        "name": "Stochastic Gradient Descent (SGD)",
        "update_rule": r"""
        \quad \mathbf{w}_{\text{new}} = \mathbf{w} - \eta v_t \\
        v_t = \beta v_{t-1} + (1 - \beta) \nabla f(\mathbf{w})
        """,
        "where": """
        - $\mathbf{w}_{\\text{new}}$ is the updated weight vector.
        - $\mathbf{w}$ is the current weight vector.
        - $\\eta$ is the learning rate.
        - $v_t$ is the momentum (velocity) term at time step $t$.
        - $\\beta$ is the momentum coefficient.
        - $v_{t-1}$ is the velocity from the previous time step.
        - $\\nabla$ $f(\mathbf{w})$ is the current gradient of the loss function with respect to the model parameters.
        
        """
    },
    "Adam": {
        "name": "Adam (Adaptive Moment Estimation)",
        "update_rule": r"""
        \quad \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon} \\
        m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla f(\mathbf{w})
        \quad v_t = \beta_2 v_{t-1} + (1 - \beta_2) \nabla f(\mathbf{w})^2
        """,
        "where": """
        - $\mathbf{w}_{\\text{new}}$ is the updated weight vector.
        - $\mathbf{w}$ is the current weight vector
        - $\\eta$ is the learning rate.
        - $\hat{m}_t$, $\hat{v}_t$ are bias-corrected first and second moment estimates.
        - $m_t$ is the first moment (mean of the gradients).
        - $v_t$ is the second moment (variance of the gradients).
        - $\\epsilon$ is a small constant to prevent division by zero.
        - $\\beta_1, \\beta_2$ are exponential decay rates for the moving averages of the first and second moments.
        - $\\nabla$ $f(\mathbf{w})$ is the current gradient of the loss function with respect to the model parameters.
        """
    },

    "RMSprop": {
        "name": "RMSprop",
        "update_rule": r"""
        \quad \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{v_t + \epsilon}} \nabla f(\mathbf{w}) \\
        v_t = \rho v_{t-1} + (1 - \rho) \nabla f(\mathbf{w})^2
        """,
        "where": """
        - $\mathbf{w}_{\\text{new}}$ is the updated weight vector.
        - $\mathbf{w}$ is the current weight vector.
        - $\\eta$ is the learning rate.
        - $v_t$ is the running average of the squared gradients.
        - $\\epsilon$ is a small constant to prevent division by zero.
        - $\\nabla$ $f(\mathbf{w})$ is the current gradient of the loss function with respect to the model parameters.
        - $\\rho$ is the decay factor.

        """
    },
        "Adagrad": {
        "name": "Adagrad",
        "update_rule": r"""
        \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{G_t} + \epsilon} \nabla f(\mathbf{w})
        """,
        "where": """
        - $\mathbf{w}_t$: The parameter vector at step \(t\).
        - $\\eta$: The learning rate.
        - $G_t$: The sum of squared gradients up to time step \(t\).
        - $\\epsilon$: A small constant to prevent division by zero.
        """
    }
}


OPTIMIZER_SETTINGS = {
    "SGD": {
         "learning_rate": 0.01,
         "momentum": 0.0,
        # "nesterov": True,
        # "weight_decay": 0.0001,  
    },
    "Adam": {
         "learning_rate": 0.001,
         "beta_1": 0.9,
         "beta_2": 0.999,
    },
    "RMSprop": {
         "learning_rate": 0.001,
         "rho": 0.9
    },
    "Adagrad": {
         "learning_rate": 0.01
    }
}
