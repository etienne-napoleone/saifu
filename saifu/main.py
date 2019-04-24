import click

from saifu import __version__
from saifu import commands


@click.group()
@click.version_option(version=__version__)
def entrypoint():
    """Saifu is a cli wallet for TomoChain and Ethereum based chains"""
    pass


entrypoint.add_command(commands.account)
entrypoint.add_command(commands.network)
