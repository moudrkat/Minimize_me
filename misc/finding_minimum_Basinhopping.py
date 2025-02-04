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