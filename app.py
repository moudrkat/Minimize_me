# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:03 2025

@author: fajma
"""

#import sys
#sys.path.append('C:\Users\fajma\Documents\Katerina_Fajmanova_Projects\Optimizer_Race')

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import core

# Function dictionary
functions = {
    "Sphere: x**2 + y**2": "x**2 + y**2",
    "Rosenbrock: (1 - x)**2 + 100 * (y - x**2)**2": "(1 - x)**2 + 100 * (y - x**2)**2",
    "Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2": "(x**2 + y - 11)**2 + (x + y**2 - 7)**2",
    "Three-hump camel: 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2":"2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2",
    "Matyas: 0.26*(x**2 + y**2) - 0.48*x*y" : "0.26*(x**2 + y**2) - 0.48*x*y",
    "Custom Function (beta version)": None,
}

def set_step(st, new_step: int) -> None:
    st.session_state.step = new_step
    st.rerun()

#streamlit app
import streamlit as st
st.title("Minimize me:red[.]")

# Initialize session state to track button clicks
if 'step' not in st.session_state:
    st.session_state.step = 1

# Display content based on the step
if st.session_state.step == 1:
        
    # Dropdown for predefined functions
    selected_function_name = st.selectbox("Choose a function:", list(functions.keys()))
    
    # Custom function input
    if selected_function_name == "Custom Function (beta version)":
        st.write("Enter a custom function in terms of x and y (e.g., x ** 2 + y ** 2 - x*y):")
        st.session_state.equation = st.text_area("Custom Function (beta version)", value="2*x**2 + 2*y**2")
    
    else:
        # Select predefined function
        st.session_state.equation = functions[selected_function_name]
        
    if st.button("Next step"):
        set_step(st, 2)
    
elif st.session_state.step == 2:
      
    try:
         st.session_state.func, st.session_state.grad_func_x, st.session_state.grad_func_y = core.get_function_and_gradients(st.session_state.equation )         
    except Exception as e: 
                st.error(f"An error occurred in function and gradient creation: {e}")
                
    try:
        
        def func_py(vars):
            x,y = vars
            return eval(st.session_state.equation )
        
        #TODO does not work but not necessary
        #all_local_minima, minimum, funcmin = core.basinhopping_find_all_minima(func_py)
        plot_container=st.container()

        with plot_container:
            figure_func_adjust, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y = core.plot_function_adjust(st.session_state.func,st.session_state.equation )
            #st.pyplot(figure_func_adjust)    
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select starting point")
                
    st.session_state.x_init=st.slider('X:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = st.session_state.max_x)
    st.session_state.y_init=st.slider('Y:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = st.session_state.max_y)

    try:
        with plot_container:
            #st.empty()
            figure_func_adjust = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y  )
            st.pyplot(figure_func_adjust)      
    except Exception as e:
            st.error(f"An error occurred in plotting: {e}")
    

                
    if st.button("Next step"):
        set_step(st, 3)
                    
    
elif st.session_state.step == 3:
           
    try:
        figure_func_start = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y )
        st.pyplot(figure_func_start)      
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select Tensorflow Optimizers")
                    
    if st.button("Minimize me."):
        set_step(st, 4)

    #TODO add optimizer selection and learning rate selection

elif st.session_state.step == 4: 
   
    try:
        def func_py(x, y):
            return eval(st.session_state.equation)
        
        #TODO animated plot 
        
        optimizers_dict = {
            "SGD": "SGD",
            "Adam": "Adam",
            "Adagrad": "Adagrad",
            "RMSprop": "RMSprop"
            }
 
    
        def run_all_optimizers(optimizers,function, x_init, y_init, lr, max_iters):
            # Store the loss history for each optimizer
            optimizer_results = {}
        
            # Loop through each optimizer and run the optimization
            for optimizer_name, optimizer_solution in optimizers.items():
                print(f"Running {optimizer_name} optimizer...")
                loss_history = core.run_optimizer(optimizer_solution, func_py, x_init, y_init, lr, max_iters)
                optimizer_results[optimizer_name] = loss_history
            
            return optimizer_results
            
        optimizer_results_for_plot = run_all_optimizers(optimizers_dict,st.session_state.func,float(st.session_state.x_init), float(st.session_state.y_init),lr=0.01,max_iters = 100)  
    except Exception as e: 
        st.error(f"An error occurred in optimizer run: {e}") 
     
    try:        
        figure = core.plot_path_history(st.session_state.func, optimizer_results_for_plot, st.session_state.equation, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y) 
        # Display the plot in Streamlit
        st.pyplot(figure)
    except Exception as e: 
        st.error(f"An error occurred in plotting: {e}") 

