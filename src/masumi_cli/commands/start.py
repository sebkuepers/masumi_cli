import typer

app = typer.Typer()

@app.command()
def main(agent_id: str, payload_file: str):
    """
    Start an agent job for a specified agent_id using the JSON payload file.
    """
    typer.echo(f"Starting job for agent: {agent_id} using payload from: {payload_file}")
    # TODO: Load payload, start the job, and capture job and payment IDs.
    typer.echo("Job started. Job ID: 123, Payment ID: 456")