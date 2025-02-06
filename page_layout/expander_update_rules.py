import streamlit as st 
from config import settings

def show_optimizer_update_rules():

    for optimizer_name, is_active in st.session_state.active_optimizers.items():
        if not is_active:
            continue
        optimizer_info = settings.optimizer_descriptions.get(optimizer_name)
        if not optimizer_info:
            continue

        st.write(f"**{optimizer_info['name']}**:") 
        # Display the explanation text
        #st.write(optimizer_info["explanation"])  # Displays the explanation text
        # Display "Update Rule" header
        #st.write("Update Rule:")
        # Display the update rule
        st.latex(optimizer_info["update_rule"])  # Displays the update rule
        # Display the components of the update rule 
        st.write("Where:")
        st.markdown(optimizer_info["where"])  # Explanation for the components of the update rule

