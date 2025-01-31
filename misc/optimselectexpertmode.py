import streamlit as st
import tensorflow as tf

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

# Streamlit UI
st.title("Select TensorFlow Optimizers")

# Checkbox for optimizers
optimizers = {
    "SGD": st.checkbox("SGD"),
    "Adam": st.checkbox("Adam"),
    "RMSProp": st.checkbox("RMSProp")
}

# Expert mode toggle
expert_mode = st.checkbox("Expert Mode")

# Show learning rate and max iterations fields if expert mode is enabled
learning_rate = None
max_iters = None
if expert_mode:
    learning_rate = st.slider("Learning Rate", min_value=1e-5, max_value=1e-1, value=1e-3, step=1e-5)
    max_iters = st.slider("Max Iterations", min_value=100, max_value=10000, value=1000, step=100)

# Create dictionary of selected optimizers
selected_optimizers = {key: value for key, value in optimizers.items() if value}

if st.button('Submit'):
    # Pass the selected optimizers and optional expert settings to your function
    optimizers_list, final_lr, final_iters = configure_optimizers(selected_optimizers, learning_rate, max_iters)
    st.write("Selected Optimizers:", optimizers_list)
    if expert_mode:
        st.write("Learning Rate:", final_lr)
        st.write("Max Iterations:", final_iters)