import click

from saifu import __version__
from saifu.commands.network import network


@click.group()
@click.version_option(version=__version__)
def entrypoint():
    """Saifu is a cli wallet for TomoChain and Ethereum based chains"""
    pass


entrypoint.add_command(network)
