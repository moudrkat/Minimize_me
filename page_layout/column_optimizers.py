import core
import streamlit as st
from config import settings

def prepare_and_run_optimizers():
    st.write("Optimizer settings:")
    # Load the active optimizers from the JSON file
    active_optimizers = core.load_active_optimizers()

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
                #st.write(f"**{optimizer_info['name']}**:") 

                if optimizer_name == "SGD":
                    col1_sgd, col2_sgd = st.columns(2)

                    with col1_sgd:
                        with st.expander("Tune SGD"):

                            optimizer_params[optimizer_name] = {
                                "learning_rate": st.select_slider("Learning Rate SGD", options=st.session_state.pos_learning_rates, value=0.001),
                                "momentum": st.slider("Momentum", min_value=0.0, max_value=1.0, value=0.9),
                                # "nesterov": st.checkbox("Use Nesterov", value=True),
                                # "weight_decay": st.number_input("Weight Decay", min_value=0.0, max_value=0.01, value=0.0001),
                                # "clipvalue": st.number_input("Clip Value", min_value=0.0, max_value=10.0, value=0.5)
                            }
                    with col2_sgd:
                        with st.expander("Show SGD update rules"):      
                            st.latex(optimizer_info["formula"])
                            st.latex(optimizer_info["momentum_formula"])
                            st.latex(optimizer_info["update_with_momentum"])

                if optimizer_name == "Adam":
                    col1_adam, col2_adam = st.columns(2)
                    with col1_adam:
                        with st.expander("Tune Adam"):
                            optimizer_params[optimizer_name] = {
                                "learning_rate": st.select_slider("Learning Rate ADAM", options=st.session_state.pos_learning_rates, value=0.001),
                                "beta_1": st.slider("Beta 1", min_value=0.5, max_value=0.99, value=0.9),
                                "beta_2": st.slider("Beta 2", min_value=0.9, max_value=0.99, value=0.999)
                            }

                    with col2_adam:
                        with st.expander("Show Adam update rules"):
                            st.latex(optimizer_info["additional_formula"])
                            st.latex(optimizer_info["corrected_moment"])
                            st.latex(optimizer_info["final_update"])
                            st.write(optimizer_info["explanation"])

    for optimizer_name, is_selected in optimizers_sel.items():
        active_optimizers[optimizer_name] = is_selected

    # Call configure_optimizers to get the optimizers with updated parameters
    st.session_state.optimizers_dict = core.configure_optimizers(optimizers_sel, optimizer_params)
    print( st.session_state.optimizers_dict)

    st.session_state.optimizer_results_for_plot = core.run_all_optimizers(st.session_state.optimizers_dict,st.session_state.equation,float(st.session_state.x_init), float(st.session_state.y_init),max_iters = st.session_state.max_iters) 
