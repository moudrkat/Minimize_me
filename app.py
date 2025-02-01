# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:03 2025

@author: fajma
"""
#import sys
#sys.path.append('C:\Users\fajma\Documents\Katerina_Fajmanova_Projects\Optimizer_Race')

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import core
import steps
from config import settings

def set_step(st, new_step: int) -> None:
    st.session_state.step = new_step
    st.rerun()

#streamlit app
import streamlit as st
st.title("Minimize me:red[.]")

# Initialize session state to track button clicks
if 'step' not in st.session_state:
    st.session_state.step = 1

# Display content based on the step
if st.session_state.step == 1:
    steps.handle_step_plain_function(settings.functions,set_step)
    
elif st.session_state.step == 2:
   steps.handle_step_start_point(set_step)
    
elif st.session_state.step == 3:
    steps.handle_step_optimizers_params(set_step)     

elif st.session_state.step == 4: 
    steps.handle_step_minimize()    


