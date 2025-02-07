import streamlit as st 
from config import settings

def show_cheatsheet():

    # display the cheatsheet for all displayed optimizers
    for optimizer_name, is_active in st.session_state.active_optimizers.items():
        if not is_active:
            continue
        #load optimizer info from config file
        optimizer_info = settings.OPTIMIZER_DESCRIPTIONS.get(optimizer_name)
        if not optimizer_info:
            continue
        #display info - formula etc for each optimizer
        st.write("") 
        st.write(f"**{optimizer_info['name']} update rules**:") 
        # Display the update rule
        st.latex(optimizer_info["update_rule"])  # Displays the update rule
        # Display the components of the update rule 
        st.write("Where:")
        st.markdown(optimizer_info["where"])  # Explanation for the components of the update rule

