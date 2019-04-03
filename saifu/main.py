import click

from saifu import __version__
from saifu.commands.networks import networks


@click.group(help=('Saifu (財布) is a cli wallet for TomoChain'))
@click.version_option(version=__version__)
def entrypoint():
    """Saifu cli entrypoint"""
    pass


entrypoint.add_command(networks)
