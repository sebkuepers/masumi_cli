import typer

app = typer.Typer()

@app.callback(invoke_without_command=True)
def agents(ctx: typer.Context):
    """
    List all local agents defined in the agents configuration in a nicely formatted table.
    """
    config = ctx.obj.get("config", {})
    agents = config.get("agents", [])
    if not agents:
        typer.echo("No local agents found.")
        raise typer.Exit(code=0)
    
    # Define a header with appropriate column widths.
    header = (
        f"{'Local ID':<8} "
        f"{'Name':<20} "
        f"{'Host':<15} "
        f"{'Port':<6} "
        f"{'Registered':<10} "
        f"{'Registered At':<25} "
        f"{'Local Path':<40} "
        f"{'Masumi ID'}"
    )
    typer.echo(header)
    typer.echo("-" * len(header))
    
    for agent in agents:
        local_id = agent.get("local_id", "")
        name = agent.get("name", "")
        host = agent.get("host", "")
        port = agent.get("port", "")
        registered = str(agent.get("registered", ""))
        # Convert None to an empty string if needed.
        registered_at = agent.get("registered_at")
        registered_at_str = registered_at if registered_at is not None else ""
        local_path = agent.get("local_path", "")
        masumi_id = agent.get("masumi_id")
        masumi_id_str = masumi_id if masumi_id is not None else ""
        
        row = (
            f"{local_id:<8} "
            f"{name:<20} "
            f"{host:<15} "
            f"{str(port):<6} "
            f"{registered:<10} "
            f"{registered_at_str:<25} "
            f"{local_path:<40} "
            f"{masumi_id_str}"
        )
        typer.echo(row)