import sympy as sp
import numpy as np

# Function to check if the symbolic derivatives exist for all variables
def check_symbolic_differentiability(f, variables):
    try:
        # Try computing the symbolic derivative for all variables
        derivatives = [sp.diff(f, var) for var in variables]
        print("Symbolic differentiation check done!")
        return True, derivatives
    except Exception as e:
        print(f"Error during symbolic differentiation: {e}")
        return False, None


# Function to numerically compute gradients using finite difference
def numerical_gradient(f, x, y, epsilon=1e-5):
    grad_x = (f(x + epsilon, y) - f(x - epsilon, y)) / (2 * epsilon)
    grad_y = (f(x, y + epsilon) - f(x, y - epsilon)) / (2 * epsilon)
    return grad_x, grad_y

# Function to check for numerical instability (e.g., NaN or Inf) in function evaluation and gradients
def check_for_numerical_instability(f, x_vals, y_vals):
    for x in x_vals:
        for y in y_vals:
            try:
                # Try evaluating the function and its gradients at each point
                value = f(x, y)
                if np.isnan(value) or np.isinf(value):
                    return False, f"Function evaluation resulted in NaN or Inf at point ({x}, {y})."
                
                # Check gradients numerically at the same point
                grad_x, grad_y = numerical_gradient(f, x, y)
                if np.isnan(grad_x) or np.isnan(grad_y) or np.isinf(grad_x) or np.isinf(grad_y):
                    return False, f"Gradients resulted in NaN or Inf at point ({x}, {y})."
            
            except Exception as e:
                return False, f"Error at point ({x}, {y}): {str(e)}"
    
    print("Numerical stability check done for all sampled points!")
    return True, None



# Function to check for vanishing or exploding gradients
def check_for_vanishing_exploding_gradients(f, x_vals, y_vals, gradient_threshold=1e10, vanishing_threshold=1e-10):
    for x in x_vals:
        for y in y_vals:
            # Compute the numerical gradients at each point
            grad_x, grad_y = numerical_gradient(f, x, y)
            
            # Check for exploding gradients (if gradients are too large)
            if np.abs(grad_x) > gradient_threshold or np.abs(grad_y) > gradient_threshold:
                return False, f"Exploding gradients at point ({x}, {y}) with gradients ({grad_x}, {grad_y})."
            
            # Check for vanishing gradients (if gradients are too small)
            if np.abs(grad_x) < vanishing_threshold and np.abs(grad_y) < vanishing_threshold:
                return False, f"Vanishing gradients at point ({x}, {y}) with gradients ({grad_x}, {grad_y})."
    
    print("Vanishing/Exploding gradient check done!")
    return True, None


# Check if function values at extreme points cause overflow/underflow
def check_for_large_inputs(f, x_vals, y_vals):
    for x in x_vals:
        for y in y_vals:
            try:
                value = f(x, y)
                if np.isnan(value) or np.isinf(value):
                    return False, f"Overflow or underflow at point ({x}, {y})."
            except Exception as e:
                return False, f"Error at point ({x}, {y}): {str(e)}"
    print("Large input check passed!")
    return True, None


# Check if function exhibits periodicity (or cyclic behavior)
def check_for_periodicity(f, x_vals, y_vals, threshold=1e-2):
    values = []
    for x in x_vals:
        for y in y_vals:
            value = f(x, y)
            values.append(value)
    
    # Check if there's significant oscillation or periodic behavior
    min_value = np.min(values)
    max_value = np.max(values)
    if (max_value - min_value) > threshold:
        return False, f"Function appears to have periodic behavior with range [{min_value}, {max_value}]."
    print("No periodic behavior detected!")
    return True, None


# Main function to validate the given function for optimization
def validate_function_for_optimization(f, variables):
    # 1. Check if the function is symbolically differentiable
    differentiable, derivatives = check_symbolic_differentiability(f, variables)
    if not differentiable:
        print("Function is not differentiable!")
        return False
    
    # 2. Check if the function and its gradients are numerically stable
    x_vals = np.linspace(-5, 5, 5)  # 5 points between -10 and 10 for x
    y_vals = np.linspace(-5, 5, 5)  # 5 points between -10 and 10 for y
    stable, error_message = check_for_numerical_instability(f, x_vals, y_vals)
    if not stable:
        print(f"Numerical instability detected: {error_message}")
        return False

    # 3. Check for large input values
    large_input_check, large_input_message = check_for_large_inputs(f, x_vals, y_vals)
    if not large_input_check:
        print(f"Large input issue detected: {large_input_message}")
        return False

    # 4. Check for periodicity
    periodic_check, periodic_message = check_for_periodicity(f, x_vals, y_vals)
    if not periodic_check:
        print(f"Periodic behavior detected: {periodic_message}")
        return False

    # 5. Check for vanishing or exploding gradients
    gradient_check, gradient_message = check_for_vanishing_exploding_gradients(f, x_vals, y_vals)
    if not gradient_check:
        print(f"Vanishing/Exploding gradient issue detected: {gradient_message}")
        return False
    
    # If all checks pass, we return True indicating the function is valid for optimization
    print("Function is valid for optimization!")
    return True


# # Example usage:
# if _name_ == "_main_":
#     # Define the function in SymPy (symbolically)
#     x, y = sp.symbols('x y')
#     f = sp.sin(x) + sp.cos(y)  # Example function: f(x, y) = sin(x) + cos(y)

#     # Validate the function for optimization
#     if validate_function_for_optimization(f, [x, y]):
#         print("Proceeding to optimization with TensorFlow...")
#         # Here, you would add your TensorFlow code to procee