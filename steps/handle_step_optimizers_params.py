import core
import streamlit as st
import tensorflow as tf
import json
from config import settings

def handle_step_optimizers_params(set_step):

    st.write("Time to let the optimizers race to find the minimum! Each optimizer has its own strategy for adjusting parameters and finding the best solution, and it's interesting to see how they perform.")
    
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

    expl = st.toggle("Further explanation")  
    optimizers_sel = {}
    for optimizer_name, is_active in active_optimizers.items():
        if is_active:
            optimizers_sel[optimizer_name] = st.checkbox(optimizer_name, value=is_active)
            if expl: 
                st.write("Explaining optimizers briefly") 

    
    # If you want to reconfigure optimizers based on selected checkboxes, update active_optimizers:
    for optimizer_name, is_selected in optimizers_sel.items():
        active_optimizers[optimizer_name] = is_selected


 

    # Expert mode toggle
    on = st.toggle("Advanced settings")
    # Show learning rate and max iterations fields if expert mode is enabled
    st.session_state.learning_rate = 0.001
    st.session_state.max_iters = 1000
    if on:
        st.write("Hyperparameter tuning activated!")
        pos_learning_rates = [0.0001,0.001,0.01]
        st.session_state.learning_rate = st.select_slider("Learning Rate (size of optimizer step)", options = pos_learning_rates, value=0.001)
        pos_max_iters = [100,1000,10000]
        st.session_state.max_iters = st.select_slider("Max Iterations (maximum number of optimizer steps)", options = pos_max_iters, value=1000)

        on_exp = st.toggle("Expert mode!")
        if on_exp:
            st.write("Super hyperparameter tuning activated!")
            st.write("""
            ### Optimization Algorithm Update Rules
            Below are the update rules for some popular optimization algorithms:
            """)

            # 1. **SGD**
            st.write("1. **Stochastic Gradient Descent (SGD)**:")
            st.latex(r"""
            \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \nabla f(\mathbf{w})
            """)

            # 2. **Adam**
            st.write("2. **Adam (Adaptive Moment Estimation)**:")
            st.latex(r"""
            m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla f(\mathbf{w})
            """)
            st.latex(r"""
            v_t = \beta_2 v_{t-1} + (1 - \beta_2) \nabla f(\mathbf{w})^2
            """)
            st.latex(r"""
            \hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
            """)
            st.latex(r"""
            \mathbf{w}_{\text{new}} = \mathbf{w} - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
            """)

            # 3. **Adagrad**
            st.write("3. **Adagrad**:")
            st.latex(r"""
            \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{G_t} + \epsilon} \nabla f(\mathbf{w})
            """)

            # 4. **RMSprop**
            st.write("4. **RMSprop**:")
            st.latex(r"""
            \mathbf{w}_{\text{new}} = \mathbf{w} - \frac{\eta}{\sqrt{v_t + \epsilon}} \nabla f(\mathbf{w})
            """)

            # Last part - variables explanation
            st.write("Where:")
            st.latex(r"""
            - \mathbf{w} = [x, y]
            - \nabla f(\mathbf{w}) = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)
            - \eta \text{ is the learning rate, and } \epsilon \text{ is a small constant to avoid division by zero.}
            """)
                

    st.session_state.optimizers_dict = configure_optimizers(optimizers_sel, st.session_state.learning_rate)
                        
    if st.button("Minimize me."):
        set_step(st, 4)