import core
import streamlit as st
import sympy as sp
import steps
from config import settings
import json
import tensorflow as tf

# Function to load the active optimizers (enabled/disabled) from the JSON file
def load_active_optimizers(file_path="active_optimizers.json"):
    with open(file_path, "r") as f:
        return json.load(f)

# Function to configure optimizers based on the active status and settings
def configure_optimizers(active_optimizers, optimizer_params=None):
    optimizers_dict = {}
    # Loop through each optimizer and check if it's active
    for optimizer_name, is_active in active_optimizers.items():
        if is_active:
            optimizer_config = settings.OPTIMIZER_SETTINGS.get(optimizer_name)
            if optimizer_config:
                # Override the optimizer config with user-defined parameters if provided
                if optimizer_params and optimizer_name in optimizer_params:
                    optimizer_config.update(optimizer_params[optimizer_name])
                # Dynamically get the optimizer class
                optimizer_class = getattr(tf.optimizers, optimizer_name)
                # Initialize the optimizer with all parameters from the config
                optimizers_dict[optimizer_name] = optimizer_class(**optimizer_config)
    return optimizers_dict