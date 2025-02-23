import typer

app = typer.Typer()

@app.command()
def main(job_id: str):
    """
    Check the status of a running job using the job_id.
    """
    typer.echo(f"Checking status for job: {job_id}")
    # TODO: Query the job status endpoint.
    typer.echo("Job status: Running")