

def handle_step_plain_function():
        # Dropdown for predefined functions
    selected_function_name = st.selectbox("Choose a function:", list(functions.keys()))
    
    # Custom function input
    if selected_function_name == "Custom Function (beta version)":
        st.write("Enter a custom function in terms of x and y (e.g., x ** 2 + y ** 2 - x*y):")
        st.session_state.equation = st.text_area("Custom Function (beta version)", value="2*x**2 + 2*y**2")
    
    else:
        # Select predefined function
        st.session_state.equation = functions[selected_function_name]
        
    if st.button("Next step"):
        set_step(st, 2)


