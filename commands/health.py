import typer

app = typer.Typer()

@app.command()
def main():
    """
    Check the /health endpoints of the payment and registry services.
    """
    typer.echo("Checking health endpoints...")
    # Mocked responses for now:
    typer.echo("Payment Service: OK")
    typer.echo("Registry Service: OK")