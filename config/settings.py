# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:05 2025

@author: fajma
"""
functions = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": "(x**2 + y - 11)**2 + (x + y**2 - 7)**2",
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": "(1 - x)**2 + 100 * (y - x**2)**2",
    #"Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": "(1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2",
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": "0.26*(x**2 + y**2) - 0.48*x*y",
    #"Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": 
    #    "-20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20",
    #"Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": 
    #    "20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))",
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": "2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2",
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": 
         "(4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2"
    #"... or be creative": None
}

ranges = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": (-5, 5, -5, 5),
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": (-2, 2, -1, 3),
    "Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": (-4, 4, -4, 4),
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": (-10, 10, -10, 10),
    "Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": (-2, 2, -2, 2),
    "Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": (-5.12, 5.12, -5.12, 5.12),
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": (-2, 2, -1.5, 1.5),
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": (-2, 2, -1, 1)
}

global_minima = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": [((3, 2), 0), ((-2.805, 3.131), 0),((-3.779, -3.283), 0),((3.584, -1.848), 0)],
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": [((1, 1), 0)],
    "Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": [((3, 0.5), 0)],
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": [((0, 0), 0)],
    "Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": [((0, 0), 0)],
    "Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": [((0, 0), 0)],
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": [((0, 0), -1.0316)],
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": [((0.0898, -0.7126), -1.0316),((-0.0898, 0.7126), -1.0316)]
}

local_minima = {
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": [],
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": [],
    "Beale: (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2": [],
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y": [],
    "Ackley: -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20": [],
    "Rastrigin: 20 + x**2 + y**2 - 10 * (cos(2 * pi * x) + cos(2 * pi * y))": [],
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2": [((-1.914,0.970), -1.031),((1.914,-0.970),-1.031)],
    "Six-hump camel: (4 - 2.1*x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4*y**2) * y**2": [((-0.089, -0.712), -1.032), ((0.089, 0.712), -1.032),((-1.732, 1.032), -0.803),((1.732, -1.032), -0.803)]
}

optimizer_descriptions = {
    "SGD": {
        "name": "Stochastic Gradient Descent (SGD)",
        "explanation": """
        Stochastic Gradient Descent (SGD) is a simple optimization algorithm that updates model parameters 
        in the direction of the negative gradient of the loss function with respect to those parameters. 
        When **momentum** is introduced, the optimizer not only considers the current gradient but also includes 
        the previous updates, effectively "remembering" past gradients to help accelerate convergence and dampen 
        oscillations.
        
        - Momentum helps in accelerating the optimization in directions with consistent gradients.
        - It also reduces oscillations in directions where gradients are noisy or vary rapidly, such as in ravines 
          or narrow valleys of the loss surface.
        """,
        "update_rule": r"""
        \quad \mathbf{w}_{\text{new}} = \mathbf{w} - \eta v_t \\
        v_t = \beta v_{t-1} + (1 - \beta) \nabla f(\mathbf{w})
        """,
        "where": """
        - $v_t$: The momentum (velocity) term at time step $t$.
        - $\beta$: The momentum coefficient, usually between 0.8 and 0.99, controlling how much of the previous gradient is remembered.
        - $v_{t-1}$: The velocity from the previous time step.
        - $\nabla$ $f(\mathbf{w})$: The current gradient of the loss function with respect to the model parameters.
        - $\eta$: The learning rate, which controls the size of each step.
        """
    },
    "Adam": {
        "name": "Adam (Adaptive Moment Estimation)",
        "explanation": """
        Adam combines the benefits of momentum and RMSprop. It adapts the learning rate for each parameter by tracking 
        the first moment (mean of the gradients) and the second moment (variance of the gradients).
        Adam also uses bias correction to avoid initial bias in the moment estimates, making it a robust choice for 
        training deep neural networks.
        """,
        "update_rule": r"""
        \quad \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon} \\
        m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla f(\mathbf{w})
        \quad v_t = \beta_2 v_{t-1} + (1 - \beta_2) \nabla f(\mathbf{w})^2
        """,
        "where": """
        - $m_t$: The first moment (mean of the gradients).
        - $v_t$: The second moment (variance of the gradients).
        - $\beta_1, \beta_2$: Exponential decay rates for the moving averages of the first and second moments.
        - $\hat{m}_t$, $\hat{v}_t$: Bias-corrected first and second moment estimates.
        - $\eta$: The learning rate.
        - $\epsilon$: A small constant to prevent division by zero.
        """
    },

    "RMSprop": {
        "name": "RMSprop",
        "explanation": """
        RMSprop modifies Adagrad by using a moving average of squared gradients, which prevents the learning rate from 
        decreasing too quickly. This makes it more stable for training non-stationary objectives, such as those found 
        in deep learning tasks with noisy data.
        """,
        "update_rule": r"""
        \quad \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{v_t + \epsilon}} \nabla f(\mathbf{w}) \\
        v_t = \rho v_{t-1} + (1 - \rho) \nabla f(\mathbf{w})^2
        """,
        "where": """
        - $v_t$: The running average of the squared gradients.
        - $\rho$: The decay factor (typically between 0.9 and 0.99).
        - $\eta$: The learning rate.
        - $\epsilon$: A small constant to prevent division by zero.
        """
    },
        "Adagrad": {
        "name": "Adagrad",
        "explanation": """
        Adagrad adjusts the learning rate based on the sum of the squared gradients. It reduces the learning rate for 
        parameters with large gradients and increases it for those with small gradients, making it well-suited for sparse data.
        """,
        "update_rule": r"""
        \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{G_t} + \epsilon} \nabla f(\mathbf{w})
        """,
        "where": """
        - $\mathbf{w}_t$: The parameter vector at step \(t\).
        - $\eta$: The learning rate.
        - $G_t$: The sum of squared gradients up to time step \(t\).
        - $\epsilon$: A small constant to prevent division by zero.
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
