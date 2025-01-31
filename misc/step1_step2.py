# -*- coding: utf-8 -*-
import streamlit as st

# Initialize session state to track button clicks
if 'step' not in st.session_state:
    st.session_state.step = 1

# Display content based on the step
if st.session_state.step == 1:
    if st.button('Step 1: Show Figure 1'):
        st.session_state.step = 2  # Move to step 2
        st.experimental_rerun()  # Rerun the app to show the next button

    # Show Figure 1
    st.image('https://via.placeholder.com/150?text=Figure+1', caption='Figure 1')

elif st.session_state.step == 2:
    if st.button('Step 2: Show Figure 2'):
        st.session_state.step = 3  # Move to the next step (optional)
        st.experimental_rerun()  # Rerun to handle next button

    # Show Figure 2
    st.image('https://via.placeholder.com/150?text=Figure+2', caption='Figure 2')