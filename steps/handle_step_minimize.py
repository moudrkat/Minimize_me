import core
import streamlit as st

def handle_step_minimize():
    try:
        def func_py(x, y):
            return eval(st.session_state.equation)
 
        def run_all_optimizers(selected_optimizers,function, x_init, y_init, lr, max_iters):
            # Store the loss history for each optimizer
            optimizer_results = {}
            #selected optimizers musi obsahvat optimizer solution a optimizer name
            # Loop through each optimizer and run the optimization
            for optimizer_name, optimizer_solution in selected_optimizers.items():
                #print(f"Running {optimizer_name} optimizer...")
                loss_history = core.run_optimizer(optimizer_solution, func_py, x_init, y_init, lr, max_iters)
                optimizer_results[optimizer_name]  = loss_history
            
            return optimizer_results
            
        optimizer_results_for_plot = run_all_optimizers(st.session_state.optimizers_dict,st.session_state.func,float(st.session_state.x_init), float(st.session_state.y_init),lr=0.01,max_iters = 100)  
    except Exception as e: 
        st.error(f"An error occurred in optimizer run: {e}") 
     
    try:        
        figure = core.plot_path_history(st.session_state.func, optimizer_results_for_plot, st.session_state.equation, st.session_state.min_x, st.session_state.min_y, st.session_state.max_x, st.session_state.max_y) 
        # Display the plot in Streamlit
        st.pyplot(figure)
    except Exception as e: 
        st.error(f"An error occurred in plotting: {e}") 
    st.write("Congratulations! You have successfully run Tensorflow optimization algorithms.")