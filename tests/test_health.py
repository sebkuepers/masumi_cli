# tests/test_health.py
import requests
from typer.testing import CliRunner
import pytest
from masumi_cli.cli import app

runner = CliRunner()

# A fake response class to simulate requests.Response
class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"Status code: {self.status_code}")

# A fake requests.get function that simulates a healthy /health/ endpoint response.
def fake_requests_get(url, headers=None):
    fake_json = {
        "status": "success",
        "data": {
            "type": "masumi-registry",
            "version": "0.1.2"
        }
    }
    return FakeResponse(fake_json)

# Monkeypatch requests.get to use our fake_requests_get.
@pytest.fixture(autouse=True)
def monkeypatch_requests_get(monkeypatch):
    monkeypatch.setattr(requests, "get", fake_requests_get)

# Override configuration loader to return a known configuration.
# Note: We patch both the original load_config and the one already imported in cli.py.
@pytest.fixture(autouse=True)
def set_config(monkeypatch):
    config_data = {
        "payment_service": {
            "url": "https://payment.example.com"
        },
        "registry_service": {
            "url": "https://registry.example.com"
        }
    }
    monkeypatch.setattr(
        "masumi_cli.utils.config.load_config",
        lambda config_path="config/default_config.yaml": config_data
    )
    monkeypatch.setattr(
        "masumi_cli.cli.load_config",
        lambda config_path="config/default_config.yaml": config_data
    )

def test_health_command():
    result = runner.invoke(app, ["health"])
    assert result.exit_code == 0, result.output
    # Now, the output should include the endpoints from our test config.
    assert "Payment Service: success (version: 0.1.2) [Endpoint: https://payment.example.com]" in result.output
    assert "Registry Service: success (version: 0.1.2) [Endpoint: https://registry.example.com]" in result.output