import core
import streamlit as st
import tensorflow as tf

def handle_step_optimizers_params(set_step):
    
    try:
        figure_func_start = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y )
        st.pyplot(figure_func_start)      
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select Tensorflow Optimizers")
        # Function that takes optimizer options as a dictionary
    def configure_optimizers(name, lr=None):
        optimizers_dict = {}
    
        if name.get('SGD', True):
            optimizers_dict['SGD'] = tf.optimizers.SGD(learning_rate=lr)
        if name.get('Adam', True):
            optimizers_dict['Adam'] = tf.optimizers.Adam(learning_rate=lr)
        if name.get('Adagrad', True):
            optimizers_dict['Adagrad'] = tf.optimizers.Adagrad(learning_rate=lr)
        if name.get('RMSProp', True):
            optimizers_dict['RMSProp'] = tf.optimizers.RMSprop(learning_rate=lr)
        # if name.get('SGD with momentum', True):
        #     optimizers_dict['SGD with momentum'] = tf.optimizers.SGD(learning_rate=lr, momentum=0.9)
    
        return optimizers_dict

    # Checkbox for optimizers
    optimizers_sel = {
        "SGD": st.checkbox("SGD",value = True),
        #"SGD with momentum": st.checkbox("SGD with momentum",value = True),
        "Adam": st.checkbox("Adam",value = True),
        "Adagrad": st.checkbox("Adagrad",value = True),
        "RMSProp": st.checkbox("RMSProp", value = True)
    }

    # Expert mode toggle
    on = st.toggle("Advanced options")
    # Show learning rate and max iterations fields if expert mode is enabled
    st.session_state.learning_rate = 0.001
    st.session_state.max_iters = 1000
    if on:
        st.write("Advance options activated!")
        st.session_state.learning_rate = st.slider("Learning Rate", min_value=1e-5, max_value=1e-1, value=1e-3, step=1e-5)
        st.session_state.max_iters = st.slider("Max Iterations", min_value=100, max_value=10000, value=1000, step=100)
        
    st.session_state.optimizers_dict = configure_optimizers(optimizers_sel, st.session_state.learning_rate)
                        
    if st.button("Minimize me."):
        set_step(st, 4)