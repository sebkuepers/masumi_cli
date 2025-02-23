import typer

app = typer.Typer()

@app.command()
def main(registration_file: str = "registration.yaml"):
    """
    Register an agent using the provided registration YAML file.
    """
    typer.echo(f"Registering agent using file: {registration_file}")
    # TODO: Load and validate the YAML file, then send the registration request (mocked).
    typer.echo("Agent registered successfully.")