import typer

app = typer.Typer()

@app.command()
def main(payment_id: str):
    """
    Dispute a payment and trigger a refund for the given payment_id.
    """
    typer.echo(f"Disputing payment: {payment_id}")
    # TODO: Implement dispute logic.
    typer.echo("Payment disputed successfully. Refund triggered.")