# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:08:03 2025

@author: fajma
"""
import os
import page_layout
import src

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

#streamlit app
import streamlit as st
st.title("Minimize me:red[.]")
st.write("Hello, I am your function f(x,y). You can minimize me using Tensorflow optimizers!")

col1, spc, col2 = st.columns([1.3,0.06, 0.9])
with col1:
    page_layout.prepare_function()

with col2:
    page_layout.prepare_and_run_optimizers()

with st.session_state.plot_container:
    figure = src.plot_function_with_start_point_and_history(st.session_state.func,st.session_state.latex_equation,st.session_state.x_init,st.session_state.y_init, st.session_state.final_min_x_max_x, st.session_state.final_min_y_max_y, st.session_state.global_minima_f,st.session_state.set_azim,st.session_state.optimizer_results_for_plot)  
    st.pyplot(figure)

with st.expander("$^*$Show Cheatsheet"):
    page_layout.show_cheatsheet()



