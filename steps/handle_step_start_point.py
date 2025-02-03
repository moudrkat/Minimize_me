import core
import streamlit as st
def handle_step_start_point(set_step):
    st.write("Here I am, ready to begin! I've set a starting point for the optimization process. This is where the search for my minimum begins.")

    try:
         st.session_state.func, st.session_state.grad_func_x, st.session_state.grad_func_y = core.get_function_and_gradients(st.session_state.equation )         
    except Exception as e: 
            st.error(f"An error occurred in function and gradient creation: {e}")
                
    try:
        
        # def func_py(vars):
        #     x,y = vars
        #     return eval(st.session_state.equation )
        
        #TODO does not work but not necessary
        #all_local_minima, minimum, funcmin = core.basinhopping_find_all_minima(func_py)
        plot_container=st.container()

        # with plot_container:
        #     figure_func_adjust, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y = core.plot_function_adjust(st.session_state.func,st.session_state.equation )
        #     #st.pyplot(figure_func_adjust)   
        st.session_state.min_x, st.session_state.max_x = st.session_state.default_min_x_max_x
        st.session_state.min_y, st.session_state.max_y = st.session_state.default_min_y_max_y

    except Exception as e:
                st.error(f"An error occurred in plotting: {e}")

    expl = st.toggle("Further explanation")
    if expl: 
        st.write("Imagine you're standing on a hill — the optimizer starts from this point and works its way down to find the lowest point. This starting point is just a 'first guess.' From here, the optimizer will adjust the values to move closer to my minimum. ")     
                
    on = st.toggle("Advanced options")
    if on:    
        st.write("Now you can select better starting point, if you want:")   
        st.session_state.x_init=st.slider('X:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = st.session_state.max_x)
        st.session_state.y_init=st.slider('Y:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = st.session_state.max_y)
        
        st.write("And you can also adjust axes ranges to zoom the function:")
        st.session_state.final_min_x_max_x=st.slider('X range:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = (st.session_state.min_x,st.session_state.max_x))
        st.session_state.final_min_y_max_y=st.slider('Y range:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = (st.session_state.min_y,st.session_state.max_y))
        st.write(st.session_state.final_min_x_max_x)
    else:
        st.session_state.x_init= st.session_state.max_x
        st.session_state.y_init= st.session_state.max_y
        st.session_state.final_min_x_max_x=(st.session_state.default_min_x_max_x)
        st.session_state.final_min_y_max_y=(st.session_state.default_min_y_max_y)

    try:
        with plot_container:
            figure_func_adjust = core.plot_function_with_start_point(st.session_state.func,st.session_state.equation,st.session_state.x_init,st.session_state.y_init, st.session_state.final_min_x_max_x, st.session_state.final_min_y_max_y, st.session_state.global_minima_f,st.session_state.local_minima_f)  
            st.pyplot(figure_func_adjust)      
    except Exception as e:
            st.error(f"An error occurred in plotting: {e}")
                
    if st.button("Proceed to optimizer selection"):
        set_step(st, 3)
                    