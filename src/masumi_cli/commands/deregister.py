import typer

app = typer.Typer()

@app.command()
def main(agent_id: str):
    """
    Deregister an agent using its agent_id.
    """
    typer.echo(f"Deregistering agent with id: {agent_id}")
    # TODO: Call the deregister endpoint (mocked).
    typer.echo("Agent deregistered successfully.")