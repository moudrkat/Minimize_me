import core
import streamlit as st
import sympy as sp
#from config import settings

def handle_step_plain_function(functions,set_step):
    st.write("Hello, I am your function f(x,y). Define my formula, and soon you'll have the chance to minimize me using different optimizers and explore how they behave!")
    on = st.toggle("Explanation")
    if on:
        st.write("Optimizers are algorithms that adjust parameters (like x and y) to make a function, such as f(x,y), as small as possible. In neural networks, this process is much more complex because there are thousands or even millions of parameters to adjust. The interesting part is that different optimizers work in different ways, and choosing the right one can speed up learning and improve the network's performance.")
        
    # Dropdown for predefined functions
    selected_function_name = st.selectbox("Select formula:", list(functions.keys()))
    
    # Custom function input
    if selected_function_name == "... or be creative":
        st.session_state.equation = st.text_area("Enter a custom formula in terms of x and y (e.g., x ** 2 + y ** 2 - x*y):", value="2*x**2 + 2*y**2")
        x, y = sp.symbols('x y')
        core.validate_function_for_optimization(sp.sympify(st.session_state.equation), [x, y])
    
    else:
        # Select predefined function
        st.session_state.equation = functions[selected_function_name]
        
    if st.button("Next step"):
        set_step(st, 2)


