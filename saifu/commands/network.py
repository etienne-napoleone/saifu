import click

from saifu.networks import NetworksManager
from saifu import views

n = NetworksManager()


@click.group()
def network():
    """Manage the different networks saifu can connect to"""
    pass


@network.command()
def ls():
    """List all available networks"""
    networks = n.list()
    if networks:
        views.network.list(networks)
    else:
        views.message.error('No network configured')


@network.command()
@click.argument('name')
@click.option('--rpc_url', prompt=f'{views.QUESTION_BULLET} Network RPC url')
@click.option('--chain_id', prompt=f'{views.QUESTION_BULLET} Network chain id')
@click.option('--ticker', prompt=f'{views.QUESTION_BULLET} Network ticker')
def add(name, rpc_url, chain_id, ticker):
    """Add a network"""
    n.new(name, rpc_url, chain_id, ticker)
    views.network.add(name, rpc_url, chain_id, ticker)


@network.command()
@click.argument('name')
def rm(name):
    """Remove a network"""
    try:
        n.rm(name)
        views.network.rm(name)
    except KeyError:
        views.message.error(f'No network found with name {name}')


@network.command()
@click.argument('name')
def select(name):
    """Select which network to connect to"""
    try:
        n.select(name)
        views.network.select(name)
    except KeyError:
        views.message.error(f'No network found with name {name}')


@network.command()
@click.argument('name')
def inspect(name):
    """Display the details of a network"""
    try:
        views.network.inspect(name, **n.get(name))
    except KeyError:
        views.message.error(f'No network found with name {name}')
