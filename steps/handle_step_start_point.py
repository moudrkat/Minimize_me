import core
import streamlit as st
def handle_step_start_point(set_step):
    st.write("Here I am, ready to begin! I've set a starting point for the optimization process. This starting point is just a 'first guess.' From here, the optimizer will adjust the values to move closer to my minimum.")

    try:
         st.session_state.func, st.session_state.grad_func_x, st.session_state.grad_func_y = core.get_function_and_gradients(st.session_state.equation )         
    except Exception as e: 
            st.error(f"An error occurred in function and gradient creation: {e}")
                     
    st.session_state.plot_container=st.container()

    st.session_state.min_x, st.session_state.max_x = st.session_state.default_min_x_max_x
    st.session_state.min_y, st.session_state.max_y = st.session_state.default_min_y_max_y
   
    st.write("Now you can select better starting point, if you want:")   
    st.session_state.x_init=st.slider('X:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = st.session_state.max_x)
    st.session_state.y_init=st.slider('Y:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = st.session_state.max_y)
    
    # st.write("And you can also adjust axes ranges to zoom me:")
    # st.session_state.final_min_x_max_x=st.slider('X range:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = (st.session_state.min_x,st.session_state.max_x))
    # st.session_state.final_min_y_max_y=st.slider('Y range:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = (st.session_state.min_y,st.session_state.max_y))

    st.session_state.final_min_x_max_x=(st.session_state.default_min_x_max_x)
    st.session_state.final_min_y_max_y=(st.session_state.default_min_y_max_y)

    # if st.button("Minimize me."):
    #     set_step(st, 3)
                    