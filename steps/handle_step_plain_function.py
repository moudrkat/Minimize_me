import core
import streamlit as st
#from config import settings

def handle_step_plain_function(functions,set_step):
    st.write("Hello, I am your function f(x,y). You can give me description and then minimize me using tesorflow optimizers.")
    on = st.toggle("Further explanation")
    if on:
        st.write("Minimizing function means thia and tensorflow optimizers mean that")
        
    # Dropdown for predefined functions
    selected_function_name = st.selectbox("Choose a function:", list(functions.keys()))
    
    # Custom function input
    if selected_function_name == "... or be creative":
        st.write("Enter a custom function in terms of x and y (e.g., x ** 2 + y ** 2 - x*y):")
        st.session_state.equation = st.text_area("Create your own function", value="2*x**2 + 2*y**2")

        #TODO add diferentiability and spelling control
    
    else:
        # Select predefined function
        st.session_state.equation = functions[selected_function_name]
        
    if st.button("Next step"):
        set_step(st, 2)


