import typer
from importlib.metadata import version, PackageNotFoundError

# Create the main Typer app
app = typer.Typer()

# Register subcommands (example, assuming you have your commands modules)
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
    show_version: bool = typer.Option(
        False,
        "--version",
        help="Show the application's version and exit.",
        is_eager=True,
    )
):
    if show_version:
        try:
            # Retrieve version info from the package metadata
            cli_version = version("masumi_cli")
        except PackageNotFoundError:
            cli_version = "0.0.0 (development)"
        typer.echo(f"Masumi CLI Version: {cli_version}")
        raise typer.Exit()

if __name__ == "__main__":
    app()