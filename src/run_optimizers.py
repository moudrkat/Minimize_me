# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:16:11 2025

@author: fajma
"""
import tensorflow as tf

def run_optimizer(optimizer,func, x_init, y_init, max_iters=1000):
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
        
def run_all_optimizers(selected_optimizers,function, x_init, y_init, max_iters):
    def func_py(x, y):
        return eval(function)
    # Store the loss history for each optimizer
    optimizer_results = {}
    # Loop through each optimizer and run the optimization
    for optimizer_name, optimizer_solution in selected_optimizers.items():
        print(f"Running {optimizer_name} optimizer...")
        loss_history = run_optimizer(optimizer_solution, func_py, x_init, y_init, max_iters)
        optimizer_results[optimizer_name]  = loss_history
    return optimizer_results
