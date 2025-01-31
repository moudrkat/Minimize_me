import core
import streamlit as st

def handle_step_optimizers_params(set_step):
    
    try:
        figure_func_start = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y )
        st.pyplot(figure_func_start)      
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select Tensorflow Optimizers")
        # Function that takes optimizer options as a dictionary
    def configure_optimizers(optimizers_dict, learning_rate=None, max_iters=None):
        optimizers = []
        if optimizers_dict.get('SGD', False):
            optimizers.append(tf.keras.optimizers.SGD(learning_rate=learning_rate))
        if optimizers_dict.get('Adam', False):
            optimizers.append(tf.keras.optimizers.Adam(learning_rate=learning_rate))
        if optimizers_dict.get('RMSProp', False):
            optimizers.append(tf.keras.optimizers.RMSprop(learning_rate=learning_rate))
        
        # Optionally, add max_iters as a custom argument if used in your setup
        return optimizers, learning_rate, max_iters

    # Checkbox for optimizers
    optimizers = {
        "SGD": st.checkbox("SGD",value = True),
        "Adam": st.checkbox("Adam",value = True),
        "RMSProp": st.checkbox("RMSProp", value = True)
    }

    # Expert mode toggle
    on = st.toggle("I want to tune hyperparameters")

    # Show learning rate and max iterations fields if expert mode is enabled
    learning_rate = 0.001
    max_iters = 1000
    if on:
        #st.write("Expert Mode activated!")
        st.session_state.learning_rate = st.slider("Learning Rate", min_value=1e-5, max_value=1e-1, value=1e-3, step=1e-5)
        st.session_state.max_iters = st.slider("Max Iterations", min_value=100, max_value=10000, value=1000, step=100)

        # Create dictionary of selected optimizers
    selected_optimizers = {key: value for key, value in optimizers.items() if value}

    # if st.button('Submit'):
    #     # Pass the selected optimizers and optional expert settings to your function
    #     optimizers_list, final_lr, final_iters = configure_optimizers(selected_optimizers, learning_rate, max_iters)
    #     st.write("Selected Optimizers:", optimizers_list)
    #     if expert_mode:
    #         st.write("Learning Rate:", final_lr)
    #         st.write("Max Iterations:", final_iters)
                        
    if st.button("Minimize me."):
        set_step(st, 4)

    #TODO add optimizer selection and learning rate selection