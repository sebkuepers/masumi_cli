import os
import yaml

def load_config(config_path: str = "config/default_config.yaml") -> dict:
    """
    Load the configuration from a YAML file.
    
    Args:
        config_path (str): Path to the YAML config file.
        
    Returns:
        dict: The configuration data.
        
    Raises:
        FileNotFoundError: If the config file is not found.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file {config_path} not found.")
    
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    return config

if __name__ == "__main__":
    # For quick testing, run this module directly.
    config = load_config()
    print("Loaded configuration:")
    print(config)