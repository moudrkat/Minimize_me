# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 08:35:59 2025

@author: fajma
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# Predefined functions
def sphere_function(x, y):
    return x**2 + y**2

def rosenbrock_function(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

def himmelblau_function(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Function dictionary
functions = {
    "Sphere Function": sphere_function,
    "Rosenbrock Function": rosenbrock_function,
    "Himmelblau Function": himmelblau_function,
    "Custom Function": None,
}

# Streamlit UI
st.title("Function Optimizer")

# Dropdown for predefined functions
selected_function_name = st.selectbox("Choose a function:", list(functions.keys()))

# Custom function input
if selected_function_name == "Custom Function":
    st.write("Enter a custom function in terms of x and y (e.g., x**2 + y**2 - x*y):")
    custom_function_input = st.text_area("Custom Function", value="x**2 + y**2")
    x, y = symbols("x y")  # Define variables for sympy
    try:
        # Parse custom function
        custom_function = sympify(custom_function_input)
        custom_function_lambdified = lambdify((x, y), custom_function, "numpy")
    except Exception as e:
        st.error(f"Error in custom function: {e}")
        custom_function_lambdified = None
else:
    # Select predefined function
    custom_function_lambdified = None
    selected_function = functions[selected_function_name]

# Generate grid for plotting
x_vals = np.linspace(-2, 2, 100)
y_vals = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)

if custom_function_lambdified:
    Z = custom_function_lambdified(X, Y)
elif selected_function_name != "Custom Function":
    Z = selected_function(X, Y)
else:
    Z = None

# Plot the selected/custom function
if Z is not None:
    fig, ax = plt.subplots()
    contour = ax.contourf(X, Y, Z, levels=50, cmap="viridis")
    ax.set_title(selected_function_name if selected_function_name != "Custom Function" else "Custom Function")
    plt.colorbar(contour)
    st.pyplot(fig)
else:
    st.warning("No function to plot. Please define a valid custom function or select one from the list.")