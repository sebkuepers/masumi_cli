import typer

app = typer.Typer()

@app.command()
def main():
    """
    List all agents (local and remote).
    """
    typer.echo("Listing agents...")
    # TODO: Read local agent definitions and query remote agents.
    typer.echo("Local Agent: agent1")
    typer.echo("Remote Agent: agent2")