streamlit_project/
├── app.py               # Main Streamlit app entry point
├── requirements.txt     # Dependencies (e.g., streamlit, numpy, matplotlib, etc.)
├── .gitignore           # Excludes unnecessary files (e.g., .env, _pycache_)
├── README.md            # Documentation about your project
├── config/              # Configuration files (optional)
│   └── settings.py      # Application-wide settings (e.g., defaults)
├── core/                # Core logic and computation modules
│   ├── _init_.py      # Makes this folder a package
│   ├── functions.py     # Classes/functions for custom functions and gradient evaluation
│   ├── optimizers.py    # Classes for optimizers 
│   └── plotting.py      # Classes or functions for 2D/3D plotting
├── tests/               # Unit tests
│   ├── _init_.py      # Makes this folder a package
│   ├── test_functions.py # Tests for functions and gradient evaluation
│   ├── test_optimizers.py # Tests for optimizer classes
│   └── test_plotting.py  # Tests for plotting functionality
├── data/                # (Optional) For storing example or testing data
│   └── sample_data.csv  # Example data file (if needed)
└── utils/               # Utility scripts and helpers
    ├── _init_.py      # Makes this folder a package
    ├── gradient_tools.py # Gradient-specific helper methods
    └── misc.py          # Miscellaneous reusable utilities