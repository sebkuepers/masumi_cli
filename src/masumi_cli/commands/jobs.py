import typer

app = typer.Typer()

@app.command()
def main():
    """
    List all jobs with their associated job and payment IDs.
    """
    typer.echo("Listing all jobs...")
    # TODO: Read from the temporary storage file and display job details.
    typer.echo("Job ID: 123, Payment ID: 456")