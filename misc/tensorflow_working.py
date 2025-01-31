# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:26:31 2025

@author: fajma
"""
import tensorflow as tf

# Example function that is differentiable
def func(x, y):
    #return (x - 3)**2 + (y - 5)**2  # A simple quadratic loss
    return eval("(x - 3)**2 + (y - 5)**2")

def gradient_descent_tf(func, x_init, y_init, lr=0.001, max_iters=1000):
    x = tf.Variable(x_init)  # Starting value for x
    y = tf.Variable(y_init)  # Starting value for y
    
    path = [(x.numpy(), y.numpy(), func(x, y).numpy())]

    # Set up the Gradient Descent optimizer with a learning rate
    optimizer = tf.optimizers.SGD(learning_rate=lr)  # Gradient Descent optimizer

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

#Test the gradient descent function
x_init = tf.constant(0.0)
y_init = tf.constant(0.0)
path = gradient_descent_tf(func, x_init, y_init, lr=0.001, max_iters=100)
print(path[-1])  # Print the final result