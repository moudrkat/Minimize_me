# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:46:00 2025

@author: fajma
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Define a simple 2D function (e.g., f(x, y) = x^2 + y^2)
def function(x, y):
    return x**2 + y**2

# Gradient of the function (used in gradient descent)
def gradient(x, y):
    grad_x = 2 * x
    grad_y = 2 * y
    return grad_x, grad_y

# Gradient Descent Optimizer
def gradient_descent(start_x, start_y, learning_rate=0.1, max_iter=100):
    x, y = start_x, start_y
    path = [(x, y)]  # Start at the initial point
    
    for _ in range(max_iter):
        grad_x, grad_y = gradient(x, y)
        
        # Update the position based on the gradient
        x = x - learning_rate * grad_x
        y = y - learning_rate * grad_y
        
        path.append((x, y))  # Append the new position to the path
        time.sleep(0.1)  # Simulate a time delay for real-time updates
        
    return path

# Adam Optimizer
def adam_optimizer(start_x, start_y, learning_rate=0.1, max_iter=100, beta1=0.9, beta2=0.999, epsilon=1e-8):
    x, y = start_x, start_y
    m_x, m_y, v_x, v_y = 0, 0, 0, 0
    path = [(x, y)]
    
    for t in range(1, max_iter + 1):
        grad_x, grad_y = gradient(x, y)
        
        m_x = beta1 * m_x + (1 - beta1) * grad_x
        m_y = beta1 * m_y + (1 - beta1) * grad_y
        v_x = beta2 * v_x + (1 - beta2) * (grad_x ** 2)
        v_y = beta2 * v_y + (1 - beta2) * (grad_y ** 2)
        
        m_hat_x = m_x / (1 - beta1 ** t)
        m_hat_y = m_y / (1 - beta1 ** t)
        v_hat_x = v_x / (1 - beta2 ** t)
        v_hat_y = v_y / (1 - beta2 ** t)
        
        x = x - learning_rate * m_hat_x / (np.sqrt(v_hat_x) + epsilon)
        y = y - learning_rate * m_hat_y / (np.sqrt(v_hat_y) + epsilon)
        
        path.append((x, y))
        time.sleep(0.1)  # Simulate real-time update
        
    return path

# Streamlit UI elements
st.title("Real-Time Optimizer Path Comparison")

# User input for starting position and learning rate
start_x = st.slider("Start X", -5, 5, 4)
start_y = st.slider("Start Y", -5, 5, -3)
learning_rate = st.slider("Learning Rate", 0.01, 0.5, 0.1)
max_iter = st.slider("Max Iterations", 10, 200, 50)

# Button to start the optimization
if st.button('Start Optimization'):
    # Run Gradient Descent (SGD)
    sgd_path = gradient_descent(start_x, start_y, learning_rate, max_iter)

    # Run Adam optimizer
    adam_path = adam_optimizer(start_x, start_y, learning_rate, max_iter)

    # Create the figure for real-time plot updates
    fig, ax = plt.subplots()

    # Create a meshgrid for contour plotting of the function
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)

    # Plot the contour of the function
    ax.contour(X, Y, Z, levels=50, cmap='coolwarm')

    # Title and labels
    ax.set_title(f"Optimizer Paths (Learning Rate: {learning_rate})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Create an empty placeholder in Streamlit for the plot
    plot_placeholder = st.empty()

    # Start the optimization and show the paths progressively for both optimizers
    for i in range(len(sgd_path)):
        # Clear the previous plot
        ax.clear()

        # Plot the contour
        ax.contour(X, Y, Z, levels=50, cmap='coolwarm')

        # Plot the path for Gradient Descent (SGD)
        sgd_x, sgd_y = zip(*sgd_path[:i+1])
        ax.plot(sgd_x, sgd_y, marker='o', color='r', markersize=5, label="Gradient Descent")

        # Plot the path for Adam
        adam_x, adam_y = zip(*adam_path[:i+1])
        ax.plot(adam_x, adam_y, marker='x', color='b', markersize=5, label="Adam")

        # Add a legend to differentiate the paths
        ax.legend()

        # Update the plot in Streamlit
        plot_placeholder.pyplot(fig)

        # Optional: Add a delay to simulate real-time animation
        time.sleep(0.1)

    st.write("Optimization complete!")