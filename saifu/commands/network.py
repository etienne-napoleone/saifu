import click

from saifu.networks import NetworksManager
from saifu import views


@click.group()
def network():
    """Manage the different networks saifu can connect to"""
    pass


@network.command()
def list():
    """List all available networks"""
    n = NetworksManager()
    views.network.list(n.list())


@network.command()
@click.option('--name', prompt=f'{views.QUESTION_BULLET} Network name')
@click.option('--rpc_url', prompt=f'{views.QUESTION_BULLET} Network RPC url')
@click.option('--chain_id', prompt=f'{views.QUESTION_BULLET} Network chain id')
@click.option('--ticker', prompt=f'{views.QUESTION_BULLET} Network ticker')
def add(name, rpc_url, chain_id, ticker):
    """Add a network"""
    n = NetworksManager()
    n.new(name, rpc_url, chain_id, ticker)
    views.network.add(name, rpc_url, chain_id, ticker)


@network.command()
@click.option('--name', prompt=f'{views.QUESTION_BULLET} Network name')
def rm(name):
    """Remove a network"""
    n = NetworksManager()
    n.rm(name)
    views.network.rm(name)


@network.command()
@click.option('--name', prompt=f'{views.QUESTION_BULLET} Network name')
def select(name):
    """Select which network to connect to"""
    n = NetworksManager()
    n.select(name)
    views.network.select(name)
