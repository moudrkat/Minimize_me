import core
import streamlit as st
import page_layout

def handle_step_minimize(set_step):
    st.write("Hello, I am your function f(x,y). Define my formula, and minimize me using Tensorflow optimizers!")

    col1, col2 = st.columns([1.3,1])
    with col1:
        page_layout.prepare_function()

    with col2:
        page_layout.prepare_and_run_optimizers()

        
    with st.session_state.plot_container:
        figure = core.plot_function_with_start_point_and_history(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.final_min_x_max_x, st.session_state.final_min_y_max_y, st.session_state.global_minima_f,st.session_state.local_minima_f,st.session_state.optimizer_results_for_plot)  
        st.pyplot(figure)



