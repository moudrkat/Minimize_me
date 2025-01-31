# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:51:47 2025

@author: fajma
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y) = x^2 + y^2
def func(x, y):
    return x**2 + y**2

# Initialize variables x and y (start at random values or specific points)
x = tf.Variable(2.0)  # Starting value for x
y = tf.Variable(3.0)  # Starting value for y

# Set up the Gradient Descent optimizer with a learning rate
optimizer = tf.optimizers.SGD(learning_rate=0.1)  # Gradient Descent optimizer

# Create lists to store the tracked values of x, y, and f(x, y)
x_values = []
y_values = []
f_values = []

# Perform optimization (minimizing the function f(x, y))
for step in range(100):
    with tf.GradientTape() as tape:
        # Record the function's output
        loss = func(x, y)
    
    # Compute the gradients of loss with respect to x and y
    grads = tape.gradient(loss, [x, y])
    
    # Apply the gradients to update x and y (gradient descent step)
    optimizer.apply_gradients(zip(grads, [x, y]))
    
    # Track the values of x, y, and f(x, y)
    x_values.append(x.numpy())
    y_values.append(y.numpy())
    f_values.append(loss.numpy())
    
    # Optionally print the values for debugging
    if step % 10 == 0:
        print(f"Step {step}: x = {x.numpy()}, y = {y.numpy()}, f(x, y) = {loss.numpy()}")

# Plot the tracked values of x, y, and f(x, y)
plt.figure(figsize=(12, 6))

# Plot x and y values over time
plt.subplot(1, 2, 1)
plt.plot(x_values, label='x values')
plt.plot(y_values, label='y values')
plt.xlabel('Step')
plt.ylabel('Value')
plt.legend()
plt.title('Tracking x and y')

# Plot f(x, y) values over time
plt.subplot(1, 2, 2)
plt.plot(f_values, label='f(x, y) values')
plt.xlabel('Step')
plt.ylabel('f(x, y)')
plt.legend()
plt.title('Tracking f(x, y)')

plt.tight_layout()
plt.show()