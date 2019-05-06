import click

from saifu.accounts import AccountsManager
from saifu.networks import NetworksManager
# from saifu import views

a = AccountsManager()
n = NetworksManager()


@click.command()
def balance():
    """Display the balance"""
    address = a.inspect(a.selected())['address']
    web3 = n.get(n.selected())
    click.echo(
        web3.fromWei(web3.eth.getBalance(address), 'ether')
    )
