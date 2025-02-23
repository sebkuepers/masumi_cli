import typer
import requests

app = typer.Typer()

def check_service_health(service_config: dict) -> dict:
    url = service_config.get("url")
    # Ensure trailing slash and append the health endpoint
    if not url.endswith("/"):
        url += "/"
    health_url = url + "health/"
    
    response = requests.get(health_url)
    response.raise_for_status()
    return response.json()

@app.callback(invoke_without_command=True)
def health(ctx: typer.Context):
    """
    Check the /health endpoints of the payment and registry services.
    """
    config = ctx.obj.get("config") if ctx.obj else {}
    if not config:
        typer.echo("No configuration loaded.")
        raise typer.Exit(code=1)
    
    payment_service_config = config.get("payment_service", {})
    registry_service_config = config.get("registry_service", {})

    try:
        payment_health = check_service_health(payment_service_config)
    except Exception as e:
        typer.echo(f"Payment Service check failed: {e}")
        payment_health = None

    try:
        registry_health = check_service_health(registry_service_config)
    except Exception as e:
        typer.echo(f"Registry Service check failed: {e}")
        registry_health = None

    payment_url = payment_service_config.get("url", "N/A")
    registry_url = registry_service_config.get("url", "N/A")

    if payment_health:
        version_str = payment_health.get("data", {}).get("version", "unknown")
        typer.echo(f"Payment Service: {payment_health.get('status')} (version: {version_str}) [Endpoint: {payment_url}]")
    else:
        typer.echo(f"Payment Service: FAILED [Endpoint: {payment_url}]")

    if registry_health:
        version_str = registry_health.get("data", {}).get("version", "unknown")
        typer.echo(f"Registry Service: {registry_health.get('status')} (version: {version_str}) [Endpoint: {registry_url}]")
    else:
        typer.echo(f"Registry Service: FAILED [Endpoint: {registry_url}]")