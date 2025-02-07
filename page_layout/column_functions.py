import src
import streamlit as st
from config import settings

def prepare_function():
    st.markdown("##### Function settings:")
    # Dropdown for predefined functions
    selected_function_name = st.selectbox("Select formula:", list(settings.FORMULAS.keys()))
    
    # Custom function input
    # if selected_function_name == "... or be creative":
    #     st.session_state.equation = st.text_area("Enter a custom formula in terms of x and y (e.g., x ** 2 + y ** 2 - x*y):", value="2*x**2 + 2*y**2")
    #     x, y = sp.symbols('x y')
    #     if st.button("Check function"):
    #         st.session_state.validation_result = core.validate_function_for_optimization(sp.sympify(st.session_state.equation), [x, y])
    #         if st.session_state.validation_result == True:
    #             st.success("Function is valid!")
    
    # else: #predefined functions dropdown here

    st.session_state.equation = settings.FORMULAS[selected_function_name]

    st.session_state.latex_equation = settings.LATEX_FORMULAS[selected_function_name]

    st.session_state.default_min_x_max_x = settings.RANGES[selected_function_name][:2] 
    st.session_state.default_min_y_max_y = settings.RANGES[selected_function_name][2:] 
    st.session_state.global_minima_f = settings.GLOBAL_MINIMA[selected_function_name]

    try:
        st.session_state.func, st.session_state.grad_func_x, st.session_state.grad_func_y = src.get_function_and_gradients(st.session_state.equation )         
    except Exception as e: 
            st.error(f"An error occurred in function and gradient creation: {e}")
                    
    st.session_state.plot_container=st.container()

    st.session_state.min_x, st.session_state.max_x = st.session_state.default_min_x_max_x
    st.session_state.min_y, st.session_state.max_y = st.session_state.default_min_y_max_y

    with st.expander("Rotate the plot"):
        st.session_state.set_degree=st.slider('↻',min_value = 0,max_value = 180, value = 0,step=5)
        st.session_state.set_azim=st.session_state.set_degree - 45

    # with st.expander("Adjust start point"):

    #     col1,col2 =st.columns(2)
    #     with col1:
    #         st.session_state.x_init=st.slider('X:',min_value = float(st.session_state.min_x),max_value = float(st.session_state.max_x), value = ((st.session_state.max_x)/2),step=0.5)
    #     with col2:
    #         st.session_state.y_init=st.slider('Y:',min_value = float(st.session_state.min_y),max_value = float(st.session_state.max_y), value = float(st.session_state.max_y),step=0.5)
        
        # st.write("And you can also adjust axes ranges to zoom me:")
        # st.session_state.final_min_x_max_x=st.slider('X range:',min_value = st.session_state.min_x,max_value = st.session_state.max_x, value = (st.session_state.min_x,st.session_state.max_x))
        # st.session_state.final_min_y_max_y=st.slider('Y range:',min_value = st.session_state.min_y,max_value = st.session_state.max_y, value = (st.session_state.min_y,st.session_state.max_y))

    st.session_state.final_min_x_max_x=(st.session_state.default_min_x_max_x)
    st.session_state.final_min_y_max_y=(st.session_state.default_min_y_max_y)