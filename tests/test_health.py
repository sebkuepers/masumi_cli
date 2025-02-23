# tests/test_health.py

from typer.testing import CliRunner
from masumi_cli.cli import app

runner = CliRunner()

def test_health_command():
    result = runner.invoke(app, ["health"])
    # Check that the command exits without errors.
    assert result.exit_code == 0, result.output
    # Verify that the expected output is in the result.
    assert "Checking health endpoints..." in result.output
    assert "Payment Service: OK" in result.output
    assert "Registry Service: OK" in result.output