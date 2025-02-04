import core
import streamlit as st
import tensorflow as tf
import json
from config import settings

def handle_step_optimizers_params(optimizer_descriptions, set_step):
    st.write("SGD proceeded to find the minimum. Now its your turn! Tune hyperparameters to get better results. Or have fun fooling SGD.")
    
    plot_container2=st.container()     
                
   #st.write("Select TensorFlow Optimizers")

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

    optimizers_sel = {}
    for optimizer_name, is_active in active_optimizers.items():
        if is_active:
            optimizers_sel[optimizer_name] = st.toggle(f"Apply {optimizer_name}")
            # Get the optimizer description from the dictionary
            st.session_state.max_iters = 1000
            optimizer_params = {}

            pos_max_iters = [100, 1000, 10000]
            st.session_state.max_iters = st.select_slider("Max Iterations (maximum number of optimizer steps)", options=pos_max_iters, value=1000)

            st.session_state.pos_learning_rates = [0.0001, 0.001, 0.01]

            # Collect custom parameters for each optimizer
            optimizer_info = optimizer_descriptions.get(optimizer_name)
            if optimizer_info:
                st.write(f"**{optimizer_info['name']}**:")
                st.latex(optimizer_info["formula"])

                if optimizer_name == "SGD":
                    st.latex(optimizer_info["momentum_formula"])
                    st.latex(optimizer_info["update_with_momentum"])

                    st.session_state.learning_rate = 0.001
    
   
                optimizer_params[optimizer_name] = {
                    "learning_rate": st.select_slider("Learning Rate (size of optimizer step)", options=st.session_state.pos_learning_rates, value=0.001),
                    "momentum": st.slider("Momentum", min_value=0.0, max_value=1.0, value=0.9),
                    # "nesterov": st.checkbox("Use Nesterov", value=True),
                    # "weight_decay": st.number_input("Weight Decay", min_value=0.0, max_value=0.01, value=0.0001),
                    # "clipvalue": st.number_input("Clip Value", min_value=0.0, max_value=10.0, value=0.5)
                }

                if optimizer_name == "Adam":
                    st.latex(optimizer_info["additional_formula"])
                    st.latex(optimizer_info["corrected_moment"])
                    st.latex(optimizer_info["final_update"])

                st.write(optimizer_info["explanation"])
                st.write("---")
                
            #     optimizer_params[optimizer_name] = {
            #         "learning_rate": st.number_input("Adam Learning Rate", min_value=0.0001, max_value=1.0, value=st.session_state.learning_rate),
            #     }

    # If you want to reconfigure optimizers based on selected checkboxes, update active_optimizers:
    for optimizer_name, is_selected in optimizers_sel.items():
        active_optimizers[optimizer_name] = is_selected


    # Call configure_optimizers to get the optimizers with updated parameters
    st.session_state.optimizers_dict = configure_optimizers(optimizers_sel, optimizer_params)

    optimizer_results_for_plot = core.run_all_optimizers(st.session_state.optimizers_dict,st.session_state.equation,float(st.session_state.x_init), float(st.session_state.y_init),lr=0.01,max_iters = 100) 
   
    with plot_container2:
        #figure = core.plot_path_history(st.session_state.func, optimizer_results_for_plot, st.session_state.equation, st.session_state.final_min_x_max_x, st.session_state.final_min_y_max_y) 
        figure = core.plot_function_with_start_point_and_history(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.final_min_x_max_x, st.session_state.final_min_y_max_y, st.session_state.global_minima_f,st.session_state.local_minima_f,optimizer_results_for_plot)  
        st.pyplot(figure)


                

