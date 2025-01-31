
def handle_step_start_point():
    try:
         st.session_state.func, st.session_state.grad_func_x, st.session_state.grad_func_y = core.get_function_and_gradients(st.session_state.equation )         
    except Exception as e: 
                st.error(f"An error occurred in function and gradient creation: {e}")
                
    try:
        
        def func_py(vars):
            x,y = vars
            return eval(st.session_state.equation )
        
        #TODO does not work but not necessary
        #all_local_minima, minimum, funcmin = core.basinhopping_find_all_minima(func_py)

        figure_func_adjust = core.plot_function_adjust(st.session_state.func,st.session_state.equation )

        st.pyplot(figure_func_adjust)    
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    st.write("Select starting point")
                
    st.session_state.x_init=st.slider('X:',min_value = -10,max_value = 10, value = 2)
    st.session_state.y_init=st.slider('Y:',min_value = -10,max_value = 10, value = 2)
                
    if st.button("Next step"):
        set_step(st, 3)