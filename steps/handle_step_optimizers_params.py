import core
import streamlit as st
import tensorflow as tf
import json
from config import settings

def handle_step_optimizers_params(optimizer_descriptions, set_step):
    st.write("Time to let the optimizers race to find the minimum! Each optimizer has its own strategy for adjusting parameters and finding the best solution, and it's interesting to see how they perform.")
    
    try:
        figure_func_start = core.plot_function_with_start_point(
            st.session_state.func, 
            st.session_state.equation,
            st.session_state.x_init,
            st.session_state.y_init, 
            st.session_state.final_min_x_max_x, 
            st.session_state.final_min_y_max_y, 
            st.session_state.global_minima_f,
            st.session_state.local_minima_f
        )  
        st.pyplot(figure_func_start)      
    except Exception as e:
        st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select TensorFlow Optimizers")

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

    expl = st.toggle("Further explanation")  
    optimizers_sel = {}
    for optimizer_name, is_active in active_optimizers.items():
        if is_active:
            optimizers_sel[optimizer_name] = st.checkbox(optimizer_name, value=is_active)
            if optimizers_sel[optimizer_name] and expl:
                # Get the optimizer description from the dictionary
                optimizer_info = optimizer_descriptions.get(optimizer_name)

                if optimizer_info:
                    st.write(f"**{optimizer_info['name']}**:")
                    st.latex(optimizer_info["formula"])

                    if optimizer_name == "SGD":
                        st.latex(optimizer_info["momentum_formula"])
                        st.latex(optimizer_info["update_with_momentum"])

                    if optimizer_name == "Adam":
                        st.latex(optimizer_info["additional_formula"])
                        st.latex(optimizer_info["corrected_moment"])
                        st.latex(optimizer_info["final_update"])

                    st.write(optimizer_info["explanation"])
                    st.write("---")

    # If you want to reconfigure optimizers based on selected checkboxes, update active_optimizers:
    for optimizer_name, is_selected in optimizers_sel.items():
        active_optimizers[optimizer_name] = is_selected

    # Expert mode toggle
    on = st.toggle("Advanced settings")
    # Show learning rate and max iterations fields if expert mode is enabled
    st.session_state.learning_rate = 0.001
    st.session_state.max_iters = 1000
    optimizer_params = {}

    if on:
        st.write("Hyperparameter tuning activated!")
        # # Allow user to select max iterations
        pos_max_iters = [100, 1000, 10000]
        st.session_state.max_iters = st.select_slider("Max Iterations (maximum number of optimizer steps)", options=pos_max_iters, value=1000)

        # For each selected optimizer, allow expert mode customization of parameters
        for optimizer_name in optimizers_sel:
            if optimizers_sel[optimizer_name]:  # Only show advanced settings if optimizer is selected
                st.subheader(f"{optimizer_name} Hyperparameters")
                st.session_state.pos_learning_rates = [0.0001, 0.001, 0.01]
                # Collect custom parameters for each optimizer
                if optimizer_name == "SGD":
                    optimizer_params[optimizer_name] = {
                        "learning_rate": st.select_slider("Learning Rate (size of optimizer step)", options=st.session_state.pos_learning_rates, value=0.001),
                        "momentum": st.slider("Momentum", min_value=0.0, max_value=1.0, value=0.9),
                        # "nesterov": st.checkbox("Use Nesterov", value=True),
                        # "weight_decay": st.number_input("Weight Decay", min_value=0.0, max_value=0.01, value=0.0001),
                        # "clipvalue": st.number_input("Clip Value", min_value=0.0, max_value=10.0, value=0.5)
                    }

                # elif optimizer_name == "Adam":
                #     optimizer_params[optimizer_name] = {
                #         "learning_rate": st.number_input("Adam Learning Rate", min_value=0.0001, max_value=1.0, value=st.session_state.learning_rate),
                #     }

    # Call configure_optimizers to get the optimizers with updated parameters
    st.session_state.optimizers_dict = configure_optimizers(optimizers_sel, optimizer_params)
    
    if st.button("Minimize me."):
        set_step(st, 4)






            # # 1. **SGD**
            # st.write("1. **Stochastic Gradient Descent (SGD)**:")
            # st.latex(r"""
            # \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \nabla f(\mathbf{w})
            # """)

            # # 2. **Adam**
            # st.write("2. **Adam (Adaptive Moment Estimation)**:")
            # st.latex(r"""
            # m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla f(\mathbf{w})
            # """)
            # st.latex(r"""
            # v_t = \beta_2 v_{t-1} + (1 - \beta_2) \nabla f(\mathbf{w})^2
            # """)
            # st.latex(r"""
            # \hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
            # """)
            # st.latex(r"""
            # \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
            # """)

            # # 3. **Adagrad**
            # st.write("3. **Adagrad**:")
            # st.latex(r"""
            # \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{G_t} + \epsilon} \nabla f(\mathbf{w})
            # """)

            # # 4. **RMSprop**
            # st.write("4. **RMSprop**:")
            # st.latex(r"""
            # \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{v_t + \epsilon}} \nabla f(\mathbf{w})
            # """)

#         #     # Last part - variables explanation
#         #     st.write("Where:")
#         #     st.latex(r"""
#         #     - \mathbf{w} = [x, y]
#         #     - \nabla f(\mathbf{w}) = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)
#         #     - \eta \text{ is the learning rate, and } \epsilon \text{ is a small constant to avoid division by zero.}
#         #     """)
                

