# tests/test_config.py

import yaml
import pytest
from masumi_cli.utils.config import load_config, load_agents_config, load_full_config

def test_load_config_success(tmp_path):
    # Create a temporary default configuration file with known content.
    config_data = {
        "payment_service": {
            "url": "https://payment.example.com",
            "access_token": "token123"
        },
        "registry_service": {
            "url": "https://registry.example.com",
            "access_token": "token456"
        }
    }
    config_file = tmp_path / "default_config.yaml"
    with open(config_file, "w") as f:
        yaml.dump(config_data, f)

    # Use load_config to load the temporary file.
    loaded_config = load_config(str(config_file))
    assert loaded_config == config_data

def test_load_config_file_not_found(tmp_path):
    # Define a file path that does not exist.
    non_existent_file = tmp_path / "nonexistent.yaml"
    with pytest.raises(FileNotFoundError):
        load_config(str(non_existent_file))

def test_load_agents_config_success(tmp_path):
    # Create a temporary agents configuration file with known content.
    agents_data = {
        "agents": [
            {
                "local_id": "a1",
                "masumi_id": "agent-001-very-long-id",
                "name": "Local Agent One",
                "host": "localhost",
                "port": 3000,
                "registered": True,
                "registered_at": "2023-03-01T12:00:00Z",
                "local_path": "/Users/sebastian/projects/agent_one"
            }
        ]
    }
    agents_file = tmp_path / "agents.yaml"
    with open(agents_file, "w") as f:
        yaml.dump(agents_data, f)

    # Use load_agents_config to load the temporary agents file.
    loaded_agents = load_agents_config(str(agents_file))
    assert loaded_agents == agents_data

def test_load_full_config_success(tmp_path):
    # Create a temporary default configuration file.
    default_config_data = {
        "payment_service": {
            "url": "https://payment.example.com",
            "access_token": "token123"
        },
        "registry_service": {
            "url": "https://registry.example.com",
            "access_token": "token456"
        }
    }
    default_config_file = tmp_path / "default_config.yaml"
    with open(default_config_file, "w") as f:
        yaml.dump(default_config_data, f)

    # Create a temporary agents configuration file.
    agents_data = {
        "agents": [
            {
                "local_id": "a1",
                "masumi_id": "agent-001-very-long-id",
                "name": "Local Agent One",
                "host": "localhost",
                "port": 3000,
                "registered": True,
                "registered_at": "2023-03-01T12:00:00Z",
                "local_path": "/Users/sebastian/projects/agent_one"
            },
            {
                "local_id": "a2",
                "masumi_id": None,
                "name": "Local Agent Two",
                "host": "localhost",
                "port": 3001,
                "registered": False,
                "registered_at": None,
                "local_path": "/Users/sebastian/projects/agent_two"
            }
        ]
    }
    agents_file = tmp_path / "agents.yaml"
    with open(agents_file, "w") as f:
        yaml.dump(agents_data, f)

    # Call load_full_config with the temporary file paths.
    full_config = load_full_config(str(default_config_file), str(agents_file))
    
    # Expect full_config to include the default config values and an "agents" key.
    expected_config = default_config_data.copy()
    expected_config["agents"] = agents_data["agents"]
    
    assert full_config == expected_config

def test_load_full_config_without_agents(tmp_path):
    # Create a temporary default configuration file.
    default_config_data = {
        "payment_service": {
            "url": "https://payment.example.com",
            "access_token": "token123"
        },
        "registry_service": {
            "url": "https://registry.example.com",
            "access_token": "token456"
        }
    }
    default_config_file = tmp_path / "default_config.yaml"
    with open(default_config_file, "w") as f:
        yaml.dump(default_config_data, f)

    # Do not create an agents configuration file.
    # load_full_config should handle this gracefully and return an empty agents list.
    full_config = load_full_config(str(default_config_file), "nonexistent_agents.yaml")
    
    expected_config = default_config_data.copy()
    expected_config["agents"] = []
    
    assert full_config == expected_config