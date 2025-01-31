# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:16:11 2025

@author: fajma
"""

import numpy as np # linear algebra
import tensorflow as tf


def run_optimizer(optimizer_name:str,func, x_init, y_init, lr=0.001, max_iters=1000):
    x = tf.Variable(tf.constant(x_init))  # Starting value for x
    y = tf.Variable(tf.constant(y_init))  # Starting value for y
    
    path = [(x.numpy(), y.numpy(), func(x, y).numpy())]

    # Set up the Gradient Descent optimizer with a learning rate
    if optimizer_name =="SGD":
         optimizer = tf.optimizers.SGD(learning_rate=lr)  # Sochastic gradient descent optimizer
    elif optimizer_name == "Adam":
        optimizer = tf.optimizers.Adam(learning_rate=lr)  # Adam optimizer
    elif optimizer_name == "Adagrad":
        optimizer = tf.optimizers.Adagrad(learning_rate=lr)  # Adam optimizer
    elif optimizer_name == "RMSprop":
        optimizer = tf.optimizers.RMSprop(learning_rate=lr)  # Adam optimizer
    else:
        raise ValueError("Wrong optimizer name")

    # Perform optimization (minimizing the function f(x, y))
    for step in range(max_iters):
        with tf.GradientTape() as tape:
            # Record the function's output
            loss = func(x, y)
        
        # Compute the gradients of loss with respect to x and y
        grads = tape.gradient(loss, [x, y])

        if grads[0] is None or grads[1] is None:
            print("No gradients provided for x or y")
            break
        
        # Apply the gradients to update x and y (gradient descent step)
        optimizer.apply_gradients(zip(grads, [x, y]))

        # Track progress
        path.append((x.numpy(), y.numpy(), loss.numpy()))
        
    return path


        # Run Nelder-Mead
        #result_nm = minimize(lambda xy: func(xy[0], xy[1]), x0=[x_init, y_init], method='Nelder-Mead')
        #path_nm = [(result_nm.x[0], result_nm.x[1], func(result_nm.x[0], result_nm.x[1]))]
        
# def gradient_descent(func, grad_func_x, grad_func_y, x_init, y_init, lr=0.001, max_iters=1000):
#     x, y = x_init, y_init
#     path = [(x, y, func(x, y))]
    
#     for _ in range(max_iters):
#         grad_x = grad_func_x(x, y)
#         grad_y = grad_func_y(x, y)
        
#         # Update using gradients
#         x -= lr * grad_x
#         y -= lr * grad_y
        
#         # Track progress
#         path.append((x, y, func(x, y)))
        
#         # Convergence check (optional)
#         #if np.sqrt(grad_x**2 + grad_y**2) < 1e-4:
#         #    break
            
#     return path
