streamlit_project/
├── app.py               # Main Streamlit app entry point
├── requirements.txt     # Dependencies (e.g., streamlit, numpy, matplotlib, etc.)
├── .gitignore           # Excludes unnecessary files (e.g., .env, _pycache_)
├── README.md            # Documentation
├── config/              # Configuration files (optional)
│   └── settings.py      # Application-wide settings (e.g., defaults)
├── core/                # Core logic and computation modules
│   ├── _init_.py        # Makes this folder a package
│   ├── functions.py     # Classes/functions for custom functions and gradient evaluation
│   ├── optimizers.py    # Classes for optimizers 
│   └── plotting.py      # Classes or functions for 2D/3D plotting
|
├──steps
|   |── handle_step_plain_function.py
|   |── handle_step_start_point
|   |── handle_step_optimizers_params
|   |── handle_step_minimize
|
├── tests/                 # Unit tests
│   ├── _init_.py          # Makes this folder a package
│   ├── test_functions.py  # Tests for functions and gradient evaluation
│   ├── test_optimizers.py # Tests for optimizer classes
│   └── test_plotting.py   # Tests for plotting functionality
