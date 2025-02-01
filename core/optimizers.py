# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:16:11 2025

@author: fajma
"""
import streamlit as st
import numpy as np # linear algebra
import tensorflow as tf

def run_optimizer(optimizer,func, x_init, y_init, lr=0.001, max_iters=1000):
    x = tf.Variable(tf.constant(x_init))  # Starting value for x
    y = tf.Variable(tf.constant(y_init))  # Starting value for y
    
    path = [(x.numpy(), y.numpy(), func(x, y).numpy())]

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
