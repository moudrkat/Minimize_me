import src
import streamlit as st
# from optimizers import OptimizerInterface
from config import settings

def prepare_and_run_optimizers():
    st.markdown("##### Optimizer settings:")


    #start point adjustment
    st.caption("Adjust start point:")
    col1,col2 =st.columns(2)
    with col1:
        st.session_state.x_init=st.slider('X:',min_value = float(st.session_state.min_x),max_value = float(st.session_state.max_x), value = ((st.session_state.max_x)/2),step=0.5)
    with col2:
        st.session_state.y_init=st.slider('Y:',min_value = float(st.session_state.min_y),max_value = float(st.session_state.max_y), value = float(st.session_state.max_y),step=0.5)
    
    #max iterations adjustment
    pos_max_iters = [100, 1000, 10000]
    st.session_state.max_iters = st.select_slider("Set max. iterations:", options=pos_max_iters, value=1000)
    optimizer_params = {}
    optimizers_sel = {}
    st.session_state.pos_learning_rates = [0.0001, 0.001, 0.01]

    # Load the active optimizers from the JSON file - by active i mean the ones depicted on webpage for selection
    st.session_state.active_optimizers = src.load_active_optimizers()

    for optimizer_name, is_active in st.session_state.active_optimizers.items():
        if not is_active:
            continue
        
        #selection of optimizer to run by the user
        optimizers_sel[optimizer_name] = st.toggle(f"RUN **{optimizer_name}** OPTIMIZER")
        # Get the optimizer description from the dictionary
        # Collect custom parameters for each optimizer
        optimizer_info = settings.OPTIMIZER_DESCRIPTIONS.get(optimizer_name)
        if not optimizer_info:
            continue

        if optimizer_name == "SGD":
            with st.expander("Tune SGD hyperparameters$^*$"):
                optimizer_params[optimizer_name] = {
                    "learning_rate": st.select_slider("$\\eta$ (learning rate SGD)", options=st.session_state.pos_learning_rates, value=0.001),
                    "momentum": st.slider("$\\beta$ (momentum coefficient)", min_value=0.0, max_value=0.9, value=0.0),
                    #"nesterov": st.checkbox("Use Nesterov", value=True),
                    }

        elif optimizer_name == "RMSprop":
            with st.expander("Tune RMSprop hyperparameters$^*$"):
                optimizer_params[optimizer_name] = {
                    "learning_rate": st.select_slider("$\\eta$ (learning rate RMSprop)", options=st.session_state.pos_learning_rates, value=0.001),
                    "rho": st.slider("$\\rho$ (decay factor)", min_value=0.9, max_value=0.99, value=0.9),
                    }

        elif optimizer_name == "Adam":
                with st.expander("Tune Adam hyperparameters$^*$"):
                    optimizer_params[optimizer_name] = {
                        "learning_rate": st.select_slider("$\\eta$ (learning Rate ADAM)", options=st.session_state.pos_learning_rates, value=0.001),
                        "beta_1": st.slider("$\\beta_1$ (decay rate for first moment)", min_value=0.5, max_value=0.99, value=0.9),
                        "beta_2": st.slider("$\\beta_2$ (decay rate for second moment)", min_value=0.9, max_value=0.99, value=0.99)
                    }

    # Call configure_optimizers to get the optimizers with updated parameters
    try:
        st.session_state.optimizers_dict = src.configure_optimizers(optimizers_sel, optimizer_params)
    except Exception as e:
        st.error(f"An error occurred in optimizer configuring: {e}")

    #Run all selected optimizers
    try:
        st.session_state.optimizer_results_for_plot = src.run_all_optimizers(st.session_state.optimizers_dict,st.session_state.equation,float(st.session_state.x_init), float(st.session_state.y_init),max_iters = st.session_state.max_iters) 
    except Exception as e:
        st.error(f"An error occurred in optimizer running: {e}")