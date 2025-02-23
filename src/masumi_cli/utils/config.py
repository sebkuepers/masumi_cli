import os
import yaml

def load_config(config_path: str = "config/default_config.yaml") -> dict:
    """
    Load the default configuration from a YAML file.
    
    Args:
        config_path (str): Path to the default YAML config file.
        
    Returns:
        dict: The configuration data.
        
    Raises:
        FileNotFoundError: If the config file is not found.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
    
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    return config

def load_agents_config(agents_config_path: str = "config/agents.yaml") -> dict:
    """
    Load the agents configuration from a YAML file.
    
    Args:
        agents_config_path (str): Path to the agents YAML config file.
        
    Returns:
        dict: The agents configuration data.
        
    Raises:
        FileNotFoundError: If the agents config file is not found.
    """
    if not os.path.exists(agents_config_path):
        raise FileNotFoundError(f"Agents configuration file '{agents_config_path}' not found.")
    
    with open(agents_config_path, "r") as f:
        agents_config = yaml.safe_load(f)
    
    return agents_config

def load_full_config(default_config_path: str = "config/default_config.yaml",
                     agents_config_path: str = "config/agents.yaml") -> dict:
    """
    Load the full configuration by merging the default configuration and the agents configuration.
    
    Returns:
        dict: A dictionary containing the default configuration along with an 'agents' key.
    """
    config = load_config(default_config_path)
    
    # Try to load agents config; if it doesn't exist, simply use an empty list.
    try:
        agents_data = load_agents_config(agents_config_path)
        # Expecting the agents YAML to have a top-level key "agents"
        config["agents"] = agents_data.get("agents", [])
    except FileNotFoundError:
        config["agents"] = []
    
    return config

if __name__ == "__main__":
    full_config = load_full_config()
    print("Loaded full configuration:")
    print(full_config)