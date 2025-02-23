# tests/test_config.py

import yaml
import pytest
from masumi_cli.utils.config import load_config

def test_load_config_success(tmp_path):
    # Create a temporary YAML config file with known content.
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

    # Use our load_config function to load the temporary file.
    loaded_config = load_config(str(config_file))
    assert loaded_config == config_data

def test_load_config_file_not_found(tmp_path):
    # Define a file path that does not exist.
    non_existent_file = tmp_path / "nonexistent.yaml"
    with pytest.raises(FileNotFoundError):
        load_config(str(non_existent_file))