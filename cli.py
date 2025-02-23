import typer

# Import command groups from the commands package
from masumi_cli.commands import health, register, deregister, agents, start, pay, dispute, status, jobs

app = typer.Typer()

# Register subcommands
app.add_typer(health.app, name="health")
app.add_typer(register.app, name="register")
app.add_typer(deregister.app, name="deregister")
app.add_typer(agents.app, name="agents")
app.add_typer(start.app, name="start")
app.add_typer(pay.app, name="pay")
app.add_typer(dispute.app, name="dispute")
app.add_typer(status.app, name="status")
app.add_typer(jobs.app, name="jobs")

if __name__ == "__main__":
    app()