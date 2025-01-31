# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np # linear algebra
#import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#import sympy
from sympy import symbols, diff, lambdify
from scipy.optimize import minimize



# Function dictionary
functions = {
    "Sphere: x**2 + y**2": "x**2 + y**2",
    #"Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": "(1 - x)**2 + 100 * (y - x**2)**2",
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": "(x**2 + y - 11)**2 + (x + y**2 - 7)**2",
    "Custom Function": None,
}


def get_function_and_gradients(func_expression):
        
     # Symbolic gradients
     grad_x = diff(func_expression, x)
     grad_y = diff(func_expression, y)
    
     # Lambdify to create Python functions
     func = lambdify((x, y), func_expression, 'numpy')
     grad_func_x = lambdify((x, y), grad_x, 'numpy')
     grad_func_y = lambdify((x, y), grad_y, 'numpy')
    
     return func, grad_func_x, grad_func_y


def gradient_descent(func, grad_func_x, grad_func_y, x_init, y_init, lr=0.01, max_iters=100):
    x, y = x_init, y_init
    path = [(x, y, func(x, y))]
    
    for _ in range(max_iters):
        grad_x = grad_func_x(x, y)
        grad_y = grad_func_y(x, y)
        
        # Update using gradients
        x -= lr * grad_x
        y -= lr * grad_y
        
        # Track progress
        path.append((x, y, func(x, y)))
        
        # Convergence check (optional)
        if np.sqrt(grad_x**2 + grad_y**2) < 1e-6:
            break
            
    return path

#streamlit app

import streamlit as st
st.title("Optimizer race")
#equation = st.text_input("enter equation")


# Dropdown for predefined functions
selected_function_name = st.selectbox("Choose a function:", list(functions.keys()))

# Custom function input
if selected_function_name == "Custom Function":
    st.write("Enter a custom function in terms of x and y (e.g., x**2 + y**2 - x*y):")
    equation = st.text_area("Custom Function", value="x**2 + y**2")

else:
    # Select predefined function
    equation = functions[selected_function_name]


# Button to plot
if st.button("Plot"):
    try:

        # # Define variables
        x, y = symbols('x y')
        
        func, grad_func_x, grad_func_y = get_function_and_gradients(equation)         
        x_init, y_init = 0, 10  # Replace with user input or random initialization
        
        # Run Gradient Descent
        path_gd = gradient_descent(func, grad_func_x, grad_func_y, x_init, y_init, lr=0.01)

        # Run Nelder-Mead
        #result_nm = minimize(lambda xy: func(xy[0], xy[1]), x0=[x_init, y_init], method='Nelder-Mead')
        #path_nm = [(result_nm.x[0], result_nm.x[1], func(result_nm.x[0], result_nm.x[1]))]

        # Convert paths to numpy arrays for plotting
        path_gd = np.array(path_gd)
        #path_nm = np.array(path_nm)
        
        # Generate data for the plot
        x_vals = np.linspace(-10, 10, 100)
        y_vals = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        
        # Safely evaluate the equation
        #Z = eval(equation)
        Z=func(X,Y)

        # Plot Convergence Paths
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

        # Plot Gradient Descent path
        ax.plot(path_gd[:, 0], path_gd[:, 1], path_gd[:, 2], color='r', label='Gradient Descent', marker='o')

        # Plot Nelder-Mead path
        #ax.plot(path_nm[:, 0], path_nm[:, 1], path_nm[:, 2], color='b', label='Nelder-Mead', marker='x')

        # Labels
        ax.set_title(f"Optimizer Convergence on {equation} Function")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("f(X, Y)")
        ax.legend()
        #plt.show()

        # Display the plot in Streamlit
        st.pyplot(fig)
    except Exception as e:
        st.error(f"An error occurred: {e}")






