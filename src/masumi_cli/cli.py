import typer
from importlib.metadata import version, PackageNotFoundError
from masumi_cli.utils.config import load_full_config  # Import the YAML loader

# Create the main Typer app
app = typer.Typer()

# Register subcommands
from masumi_cli.commands import health, register, deregister, agents, start, pay, dispute, status, jobs
app.add_typer(health.app, name="health")
app.add_typer(register.app, name="register")
app.add_typer(deregister.app, name="deregister")
app.add_typer(agents.app, name="agents")
app.add_typer(start.app, name="start")
app.add_typer(pay.app, name="pay")
app.add_typer(dispute.app, name="dispute")
app.add_typer(status.app, name="status")
app.add_typer(jobs.app, name="jobs")

@app.callback()
def main(
    ctx: typer.Context,
    show_version: bool = typer.Option(
        False,
        "--version",
        help="Show the application's version and exit.",
        is_eager=True,
    )
):
    if show_version:
        try:
            cli_version = version("masumi_cli")
        except PackageNotFoundError:
            cli_version = "0.0.0 (development)"
        typer.echo(f"Masumi CLI Version: {cli_version}")
        raise typer.Exit()

    # Load configuration once and store it in the context
    try:
        config = load_full_config()
    except Exception as e:
        typer.echo(f"Error loading configuration: {e}")
        raise typer.Exit(code=1)
    
    ctx.obj = {"config": config}

if __name__ == "__main__":
    app()