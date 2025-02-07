# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:11 2025

@author: fajma
"""
import sympy as sp
from sympy import symbols, diff, lambdify

x, y = symbols('x y')

# sympify user selected function and create gradients
def get_function_and_gradients(func_expression):
    func_expression = sp.sympify(func_expression)
    # Symbolic gradients
    grad_x = diff(func_expression, x)
    grad_y = diff(func_expression, y)
    # Lambdify to create Python functions
    func = lambdify((x, y), func_expression, 'numpy')
    grad_func_x = lambdify((x, y), grad_x, 'numpy')
    grad_func_y = lambdify((x, y), grad_y, 'numpy')
    return func, grad_func_x, grad_func_y
