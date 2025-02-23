import typer

app = typer.Typer()

@app.callback(invoke_without_command=True)
def health(ctx: typer.Context):
    """
    Check the /health endpoints of the payment and registry services.
    """
    # If no subcommand is provided, run the default behavior:
    if ctx.invoked_subcommand is None:
        typer.echo("Checking health endpoints...")
        # Mocked responses for now:
        typer.echo("Payment Service: OK")
        typer.echo("Registry Service: OK")