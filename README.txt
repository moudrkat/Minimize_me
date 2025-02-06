streamlit_project/
├── app.py                      # Main Streamlit app entry point
├── requirements.txt            # Dependencies 
├── .gitignore                  # Excludes unnecessary files 
├── README.md                   # Documentation
│
├── config/                     # Configuration files
│   └── settings.py             # Application-wide settings (e.g., defaults)
│   └── active_optimizers.json
│
├── src/                        # Core logic and computation modules
│   ├── _init_.py       
│   ├── functions.py            # Classes/functions for custom functions and gradient evaluation
│   ├── run_optimizers.py       # Classes for optimizers 
│   └── plotting.py             # Classes or functions for 2D/3D plotting
│
|── page_layout/
├   ├── _init_.py        
├   ├── column_functions
├   ├── column_optimizers
├   ├── expander_update_rules
│
├── tests/                      # Unit tests
│   ├── _init_.py          
│   ├── tests.py                # Tests




The aim of this app is to give the user opportunity to compare Tensorflow optimizers paths on via visualisation on f(x,y) surface.

