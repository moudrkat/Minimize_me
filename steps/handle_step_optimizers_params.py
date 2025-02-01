import core
import streamlit as st
import tensorflow as tf
import json
from config import settings

def handle_step_optimizers_params(set_step):
    
    try:
        figure_func_start = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y )
        st.pyplot(figure_func_start)      
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select Tensorflow Optimizers")

    # Function to load the active optimizers (enabled/disabled) from the JSON file
    def load_active_optimizers(file_path="active_optimizers.json"):
        with open(file_path, "r") as f:
            return json.load(f)

    # Function to configure optimizers based on the active status and settings
    def configure_optimizers(active_optimizers, lr=None):
        optimizers_dict = {}

        # Loop through each optimizer and check if it's active
        for optimizer_name, is_active in active_optimizers.items():
            if is_active:
                optimizer_config = settings.OPTIMIZER_SETTINGS.get(optimizer_name)
                if optimizer_config:
                    optimizer_class = getattr(tf.optimizers, optimizer_name)  # Dynamically get the optimizer class
                    optimizers_dict[optimizer_name] = optimizer_class(learning_rate=lr or optimizer_config["learning_rate"])

        return optimizers_dict

    # Load the active optimizers from the JSON file
    active_optimizers = load_active_optimizers()

    optimizers_sel = {}
    for optimizer_name, is_active in active_optimizers.items():
        if is_active:
            optimizers_sel[optimizer_name] = st.checkbox(optimizer_name, value=is_active)

    # If you want to reconfigure optimizers based on selected checkboxes, update active_optimizers:
    for optimizer_name, is_selected in optimizers_sel.items():
        active_optimizers[optimizer_name] = is_selected

    expl = st.toggle("Further explanation")
    if expl: 
        st.write("Explaining optimizers briefly")   

        equa = st.toggle("Show brutal equations")
        if equa: 
            st.write("Showing brutal equations")

    # Expert mode toggle
    on = st.toggle("Expert options")
    # Show learning rate and max iterations fields if expert mode is enabled
    st.session_state.learning_rate = 0.001
    st.session_state.max_iters = 1000
    if on:
        st.write("Hyperparameter tuning activated!")
        st.session_state.learning_rate = st.slider("Learning Rate", min_value=1e-5, max_value=1e-1, value=1e-3, step=1e-5)
        st.session_state.max_iters = st.slider("Max Iterations", min_value=100, max_value=10000, value=1000, step=100)

    st.session_state.optimizers_dict = configure_optimizers(optimizers_sel, st.session_state.learning_rate)
                        
    if st.button("Minimize me."):
        set_step(st, 4)