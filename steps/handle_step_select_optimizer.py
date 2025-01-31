

def handle_step_select_optimizer()
    
        try:
        figure_func_start = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init)
        st.pyplot(figure_func_start)      
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select Tensorflow Optimizers")
                    
    if st.button("Minimize me."):
        set_step(st, 4)

    #TODO add optimizer selection and learning rate selection