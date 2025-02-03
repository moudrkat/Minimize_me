# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:16:33 2025

@author: fajma
"""

import numpy as np # linear algebra
from scipy.optimize import minimize
import matplotlib.pyplot as plt

from scipy.optimize import basinhopping

#TODO doesnt work
def basinhopping_find_all_minima(func):
    
    # List to store all local minima found
    local_minima = []
    global_minimum = None

    # Define the callback function to track local minima
    def track_minima(x, f, accepted):
        nonlocal global_minimum
        if accepted:
            # Store each accepted local minimum
            local_minima.append((x, f))
            # Update the global minimum if necessary
            if global_minimum is None or f < global_minimum[1]:
                global_minimum = (x, f)  # Update with the new global minimum

    # Initial guess
    initial_guess = [1.0, 1.0]

    # Run basinhopping with the callback function
    result = basinhopping(func, initial_guess, callback=track_minima)

    # Output all the local minima found
    print("All local minima found during the process:")
    for minima in local_minima:
        print(f"Point: {minima[0]}, Function Value: {minima[1]}")
        
    # Final result
    print("\nGlobal Minimum Found:")
    print(f"Point: {result.x}, Function Value: {result.fun}")
    
    return local_minima, global_minimum, result


def plot_function_with_start_point(func_to_optimize, equation, x_init, y_init, x_range, y_range, global_minima, local_minima):
    # Unpack the x and y ranges
    min_x, max_x = x_range
    min_y, max_y = y_range

    # Generate data for the plot
    x_vals = np.linspace(min_x, max_x, 1000)
    y_vals = np.linspace(min_y, max_y, 1000)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = func_to_optimize(X, Y)

    fig = plt.figure(figsize=(12, 8))

    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

    # Plot the initial starting point
    ax.scatter(x_init, y_init, func_to_optimize(x_init, y_init), color='r', s=30)

    # for (min_x, min_y), _ in global_minima:
    #     min_val = func_to_optimize(min_x, min_y)  # Evaluate function at the minima
    #     ax.scatter(min_x, min_y, 0, color='r', s=30, label='Global Minima')

    # for (min_x, min_y), _ in local_minima:
    #     min_val = func_to_optimize(min_x, min_y)  # Evaluate function at the minima
    #     ax.scatter(min_x, min_y, 0, color='b', s=30, label='Local Minima')

    # Contour plot
    contour = ax.contour(X, Y, Z, 20, cmap='coolwarm', offset=np.min(Z)-0.5)

    # Set the aspect ratio of the plot
    #ax.set_box_aspect([1, 1, 1])

    #ax.set_xlim(min_x, max_x)
    #ax.set_ylim(min_y, max_y)
    # ax.set_zlim(np.min(Z), np.max(Z))
    # Labels
    ax.set_title(f"{equation}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("f(X, Y)")
    ax.legend()

    return fig

def plot_path_history(func_to_optimize, optimizer_results, equation, x_range, y_range):
    # Unpack the x and y ranges
    min_x, max_x = x_range
    min_y, max_y = y_range

    # Generate data for the plot
    x_vals = np.linspace(min_x, max_x, 1000)
    y_vals = np.linspace(min_y, max_y, 1000)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = func_to_optimize(X, Y)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

    # Contour plot
    contour = ax.contour(X, Y, Z, 20, cmap='coolwarm', offset=np.min(Z)-0.5)

    # Plot optimizer paths
    for optimizer_name, loss_history in optimizer_results.items():
        path_optimizer = np.array(loss_history)
        ax.plot(path_optimizer[:, 0], path_optimizer[:, 1], path_optimizer[:, 2], label=optimizer_name, marker='o')

    # Labels
    ax.set_title(f"Optimizer Convergence on {equation} Function")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("f(X, Y)")
    ax.legend()

    return fig


    
    