# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:16:33 2025

@author: fajma
"""

import numpy as np # linear algebra
import matplotlib.pyplot as plt

def plot_function_with_start_point_and_history(func_to_optimize, equation, x_init, y_init, x_range, y_range, global_minima, local_minima, optimizer_results=None):
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
    # Plot the surface
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)
    # Plot the initial starting point
    ax.scatter(x_init, y_init, func_to_optimize(x_init, y_init), color='r', s=30,label='Start point')
    # Flags to check if labels have been added
    label_added_global = False
    label_added_local = False
    # Plot global minima
    for (min_x, min_y), _ in global_minima:
        min_val = func_to_optimize(min_x, min_y)  # Evaluate function at the minima
        if not label_added_global:
            ax.scatter(min_x, min_y, min_val, color='r', s=30, marker='x', label='Global Minimum')
            label_added_global = True
        else:
            ax.scatter(min_x, min_y, min_val, color='r', s=30, marker='x')

    # Plot local minima (commended out because its confusing)
    # for (min_x, min_y), _ in local_minima:
    #     min_val = func_to_optimize(min_x, min_y)  # Evaluate function at the minima
    #     if not label_added_local:
    #         ax.scatter(min_x, min_y, min_val, color='b', s=30, marker='x', label='Local Minimum')
    #         label_added_local = True
    #     else:
    #         ax.scatter(min_x, min_y, min_val, color='b', s=30, marker='x')

    # If optimizer path history is provided, plot it
    if optimizer_results:
        # Contour plot for visual reference
        ax.contour(X, Y, Z, 20, cmap='coolwarm', offset=np.min(Z)-0.5)
        # Plot optimizer paths
        for optimizer_name, loss_history in optimizer_results.items():
            path_optimizer = np.array(loss_history)
            ax.plot(path_optimizer[:, 0], path_optimizer[:, 1], path_optimizer[:, 2], label=optimizer_name, marker='o')
    # Labels
    ax.set_title(f"{equation}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("f(X, Y)")
    # Add legend to the plot
    ax.legend()
    return fig



    
    