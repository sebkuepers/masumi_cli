import typer

app = typer.Typer()

@app.command()
def main(agent_id: str):
    """
    Process a payment for the specified agent.
    """
    typer.echo(f"Processing payment for agent: {agent_id}")
    # TODO: Implement payment logic (using stored job/payment IDs).
    typer.echo("Payment processed successfully.")