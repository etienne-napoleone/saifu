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


@networks.command()
@click.option('--name', prompt=f'{views.QUESTION_BULLET} Network name')
@click.option('--rpc_url', prompt=f'{views.QUESTION_BULLET} Network RPC url')
@click.option('--chain_id', prompt=f'{views.QUESTION_BULLET} Network chain id')
@click.option('--ticker', prompt=f'{views.QUESTION_BULLET} Network ticker')
def add(name, rpc_url, chain_id, ticker):
    n = NetworksManager()
    n.new(name, rpc_url, chain_id, ticker)
    views.networks.add(name, rpc_url, chain_id, ticker)


@networks.command()
@click.option('--name', prompt=f'{views.QUESTION_BULLET} Network name')
def rm(name):
    n = NetworksManager()
    n.rm(name)
    views.networks.rm(name)


@networks.command()
@click.option('--name', prompt=f'{views.QUESTION_BULLET} Network name')
def select(name):
    n = NetworksManager()
    n.select(name)
    views.networks.select(name)
