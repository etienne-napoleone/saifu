import click

from saifu.networks import NetworksManager
from saifu import views


@click.group()
def networks():
    pass


@networks.command()
def list():
    n = NetworksManager()
    views.networks.list(n.list())
