streamlit_project/
├── app.py                                    # Main entry point for the Streamlit app
├── requirements.txt                          # Python dependencies for the app
├── .gitignore                                # Specifies files to exclude from version control
├── README.md                                 # Project documentation
│
├── config/                                   # Configuration files for the app
│   ├── __init__.py                           # Initialization of the configuration module
│   ├── settings.py                           # Contains function definitions, minima, ranges, and optimizer settings (default parameters, cheatsheet data)
│   ├── active_optimizers.json                # Stores the active optimizers used in the deployed app (with True/False values)
│   └── Exploding_gradient.jpg                # "Easter egg" image for the app
│
├── src/                                      # Core logic and computation modules
│   ├── __init__.py                           # Initialization of the source module
│   ├── functions.py                          # Handles function selection, custom function support (for future versions), and gradient evaluation
│   ├── load_and_configure_optimizers.py      # Configures optimizers with selected hyperparameters
│   ├── run_optimizers.py                     # Runs TensorFlow optimizers with selected settings
│   └── plotting.py                           # 3D plotting functions for visualizing optimization paths
│
├── page_layout/                              # Streamlit frontend logic for page layout and display
│   ├── __init__.py                           # Initialization of the page layout module
│   ├── column_functions.py                   # Function selection and plotting display components
│   ├── column_optimizers.py                  # Optimizer control, execution, and hyperparameter tuning components
│   ├── expander_cheatsheet.py                # Bottom section containing the optimizer update rules cheatsheet
│
├── unused_scripts/                           # Miscellaneous or experimental scripts for future app versions


Welcome to the "Minimize me." app! This interactive tool allows you to observe and explore how TensorFlow optimizers search for the minimum of a mathematical function, such as the Rosenbrock function.

Features
    Interactive Optimization: Watch TensorFlow optimizers in action as they minimize the function.
    Hyperparameter Tuning: Adjust and experiment with key optimization parameters like learning rate, number of iterations, and batch size to observe their impact on the optimization process.
    Visualization: Visualize the optimizer's path as it traverses the function landscape. You can rotate the plot to get a better view of the optimization process.
    Real-Time Feedback: Instantly see how your changes to the hyperparameters influence the optimizer's behavior.

Planned Future Features
    In future versions of the app, I plan to introduce several exciting features based on user interest and feedback:

    Custom Function Support: Ability to write and optimize your own custom functions.
    Additional Optimizers: More optimization algorithms will be available, offering greater flexibility for experimentation.

    These features will be implemented if there is sufficient demand and interest from users. If you’d like to see these additions, please let me know through feedback!

How to Use
    Left side:
        Select a Function: Begin by selecting the function you wish to optimize from the available options. 
        Rotate the Plot: Once the function is loaded, you can rotate the plot to view the optimization process from different angles for a better understanding of the path taken by the optimizer.

    Right side:
        Adjust the Start Point: You can specify a starting point for the optimization process. The optimizers will begin their search for the minimum from this point.
        Set Maximum Iterations: Control how many iterations the optimizer will perform. This setting determines how long the optimization will run.
        Run Optimizers: On the right side of the app, you’ll find toggle buttons for each optimizer (e.g., SGD, Adam). Turn on the toggle for the optimizer you want to run
        Tune Hyperparameters: Under each optimizer’s section, you'll find an expander containing hyperparameters that can be fine-tuned (e.g., learning rate). Experiment with different values to observe how they affect the optimizer’s behavior.

    Footer:
        Refer to the Cheatsheet: If you want to recall the update rules or formulas used by each optimizer, you can access a handy cheatsheet at the bottom expander of the app. This section provides the relevant formulas for each optimization method.
