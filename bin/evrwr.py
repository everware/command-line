import click


@click.group()
def cli():
    pass


@cli.command()
def init():
    """Create the basic everware structure"""
    click.echo('Initialized everware!')


if __name__ == "__main__":
    cli()
