import core
import streamlit as st
import sympy as sp
import steps
from config import settings
import json
import tensorflow as tf
from config import settings

def handle_step_plain_function(functions, ranges, global_minima, local_minima, set_step):
    st.write("Hello, I am your function f(x,y). Define my formula, and soon you'll have the chance to minimize me using stochastic gradient descent (SGD) and tune hyperparameters!")
 
    # Dropdown for predefined functions
    selected_function_name = st.selectbox("Select formula:", list(functions.keys()))
    
    # Custom function input
    # if selected_function_name == "... or be creative":
    #     st.session_state.equation = st.text_area("Enter a custom formula in terms of x and y (e.g., x ** 2 + y ** 2 - x*y):", value="2*x**2 + 2*y**2")
    #     x, y = sp.symbols('x y')

    #     #button_check_clicked = False
    #     if st.button("Check function"):
    #         st.session_state.function_checked = True

    #     if "function_checked" in st.session_state:
    #         st.session_state.validation_result = core.validate_function_for_optimization(sp.sympify(st.session_state.equation), [x, y])
    #         #validation = core.validate_function_for_optimization(sp.sympify(st.session_state.equation), [x, y])
    #         if st.session_state.validation_result == True:
    #             st.success("Function is valid!")
    
    # else:
        # Select predefined function
    st.session_state.equation = functions[selected_function_name]
    st.session_state.default_min_x_max_x = ranges[selected_function_name][:2] 
    st.session_state.default_min_y_max_y = ranges[selected_function_name][2:] 

    st.session_state.global_minima_f = global_minima[selected_function_name]
    st.session_state.local_minima_f = local_minima[selected_function_name]

    st.write("Here I am, ready to begin! I've set a starting point for the optimization process. This starting point is just a 'first guess.' From here, the optimizer will adjust the values to move closer to my minimum.")

    try:
         st.session_state.func, st.session_state.grad_func_x, st.session_state.grad_func_y = core.get_function_and_gradients(st.session_state.equation )         
    except Exception as e: 
            st.error(f"An error occurred in function and gradient creation: {e}")
                     
    st.session_state.plot_container=st.container()

    st.session_state.min_x, st.session_state.max_x = st.session_state.default_min_x_max_x
    st.session_state.min_y, st.session_state.max_y = st.session_state.default_min_y_max_y
   
    with st.expander("Adjust start point"):
        st.write("Now you can select better starting point, if you want:")   
        st.session_state.x_init=st.slider('X:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = st.session_state.max_x)
        st.session_state.y_init=st.slider('Y:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = st.session_state.max_y)
        
        # st.write("And you can also adjust axes ranges to zoom me:")
        # st.session_state.final_min_x_max_x=st.slider('X range:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = (st.session_state.min_x,st.session_state.max_x))
        # st.session_state.final_min_y_max_y=st.slider('Y range:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = (st.session_state.min_y,st.session_state.max_y))

    st.session_state.final_min_x_max_x=(st.session_state.default_min_x_max_x)
    st.session_state.final_min_y_max_y=(st.session_state.default_min_y_max_y)

    st.write("Lets run the optimizers")

    # Function to load the active optimizers (enabled/disabled) from the JSON file
    def load_active_optimizers(file_path="active_optimizers.json"):
        with open(file_path, "r") as f:
            return json.load(f)

    # Function to configure optimizers based on the active status and settings
    def configure_optimizers(active_optimizers, optimizer_params=None):
        optimizers_dict = {}
        # Loop through each optimizer and check if it's active
        for optimizer_name, is_active in active_optimizers.items():
            if is_active:
                optimizer_config = settings.OPTIMIZER_SETTINGS.get(optimizer_name)
                if optimizer_config:
                    # Override the optimizer config with user-defined parameters if provided
                    if optimizer_params and optimizer_name in optimizer_params:
                        optimizer_config.update(optimizer_params[optimizer_name])
                    # Dynamically get the optimizer class
                    optimizer_class = getattr(tf.optimizers, optimizer_name)
                    # Initialize the optimizer with all parameters from the config
                    optimizers_dict[optimizer_name] = optimizer_class(**optimizer_config)
        return optimizers_dict

    # Load the active optimizers from the JSON file
    active_optimizers = load_active_optimizers()

    pos_max_iters = [100, 1000, 10000]
    st.session_state.max_iters = st.select_slider("Max Iterations (maximum number of optimizer steps)", options=pos_max_iters, value=1000)
    optimizer_params = {}
    optimizers_sel = {}
    st.session_state.pos_learning_rates = [0.0001, 0.001, 0.01]

    for optimizer_name, is_active in active_optimizers.items():
        if is_active:
            optimizers_sel[optimizer_name] = st.toggle(f"RUN ({optimizer_name}) OPTIMIZER")
            # Get the optimizer description from the dictionary
            # Collect custom parameters for each optimizer
            optimizer_info = settings.optimizer_descriptions.get(optimizer_name)
            if optimizer_info:
                st.write(f"**{optimizer_info['name']}**:") 

                if optimizer_name == "SGD":
                    col1, col2 = st.columns(2)

                    with col1:
                        with st.expander("Tune SGD hyperparameters"):
    
                            optimizer_params[optimizer_name] = {
                                "learning_rate": st.select_slider("Learning Rate (size of optimizer step)", options=st.session_state.pos_learning_rates, value=0.001),
                                "momentum": st.slider("Momentum", min_value=0.0, max_value=1.0, value=0.9),
                                # "nesterov": st.checkbox("Use Nesterov", value=True),
                                # "weight_decay": st.number_input("Weight Decay", min_value=0.0, max_value=0.01, value=0.0001),
                                # "clipvalue": st.number_input("Clip Value", min_value=0.0, max_value=10.0, value=0.5)
                            }
                    with col2:
                            with st.expander("Show SGD update rules"):      
                                st.latex(optimizer_info["formula"])
                                st.latex(optimizer_info["momentum_formula"])
                                st.latex(optimizer_info["update_with_momentum"])



                if optimizer_name == "Adam":
                    col1, col2 = st.columns(2)
                    with col1:
                        with st.expander("Tune Adam hyperparameters"):
                            optimizer_params[optimizer_name] = {
                                "learning_rate": st.select_slider("Learning Rate", options=st.session_state.pos_learning_rates, value=0.001),
                                "beta_1": st.slider("Beta 1", min_value=0.5, max_value=0.99, value=0.9),
                                "beta_2": st.slider("Beta 2", min_value=0.9, max_value=0.99, value=0.999)
                            }

                    with col2:
                        with st.expander("Show Adam update rules"):
                            st.latex(optimizer_info["additional_formula"])
                            st.latex(optimizer_info["corrected_moment"])
                            st.latex(optimizer_info["final_update"])

                            st.write(optimizer_info["explanation"])
                            st.write("---")



    for optimizer_name, is_selected in optimizers_sel.items():
        active_optimizers[optimizer_name] = is_selected

    # Call configure_optimizers to get the optimizers with updated parameters
    st.session_state.optimizers_dict = configure_optimizers(optimizers_sel, optimizer_params)

    optimizer_results_for_plot = core.run_all_optimizers(st.session_state.optimizers_dict,st.session_state.equation,float(st.session_state.x_init), float(st.session_state.y_init),max_iters = st.session_state.max_iters) 
   
    with st.session_state.plot_container:
        figure = core.plot_function_with_start_point_and_history(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.final_min_x_max_x, st.session_state.final_min_y_max_y, st.session_state.global_minima_f,st.session_state.local_minima_f,optimizer_results_for_plot)  
        st.pyplot(figure)
    #steps.handle_step_start_point(set_step)
    #steps.handle_step_optimizers_params(settings.optimizer_descriptions, set_step)     

    # if st.button("Plot me."):
    #     set_step(st, 2)


