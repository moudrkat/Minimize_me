import core
import streamlit as st
def handle_step_start_point(set_step):
    st.write("Great choice! The optimization will start at the red point.")
    expl = st.toggle("Further explanation")
    if expl: 
         st.write("Optimizers need start point.")     

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
        plot_container=st.container()

        with plot_container:
            figure_func_adjust, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y = core.plot_function_adjust(st.session_state.func,st.session_state.equation )
            #st.pyplot(figure_func_adjust)    
    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")
                
    on = st.toggle("Start point adjustment")
    if on:       
        st.session_state.x_init=st.slider('X:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = st.session_state.max_x)
        st.session_state.y_init=st.slider('Y:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = st.session_state.max_y)
    else:
        st.session_state.x_init= st.session_state.max_x
        st.session_state.y_init= st.session_state.max_y
    try:
        with plot_container:
            figure_func_adjust = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y  )
            st.pyplot(figure_func_adjust)      
    except Exception as e:
            st.error(f"An error occurred in plotting: {e}")
                
    if st.button("Next step"):
        set_step(st, 3)
                    