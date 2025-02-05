# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:03 2025

@author: fajma
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import steps
from config import settings

def set_step(st, new_step: int) -> None:
    st.session_state.step = new_step
    st.rerun()

#streamlit app
import streamlit as st
st.title("Minimize me:red[.]")

if 'step' not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    steps.handle_step_plain_function(settings.functions, settings.ranges, settings.global_minima, settings.local_minima, set_step)
    
#elif st.session_state.step == 2:
    #handle step export

#TODO add export



