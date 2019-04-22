import click

from saifu.accounts import AccountsManager
from saifu import views

n = AccountsManager()


@click.group()
def account():
    """Manage the different accounts saifu can use"""
    pass


@account.command()
def ls():
    """List all available accounts"""
    accounts = n.list()
    if accounts:
        views.account.list(accounts)
    else:
        views.message.error('No account configured')


@account.command()
@click.argument('name')
@click.option('--pkey', prompt=f'{views.QUESTION_BULLET} Private key', hide_input=True)  # noqa: E501
@click.option('--password', prompt=f'{views.QUESTION_BULLET} Password', hide_input=True)  # noqa: E501
def add(name, pkey, password):
    """Add an account"""
    n.new(name, pkey, password)


@account.command()
@click.argument('name')
def rm(name):
    """Remove an account"""
    pass


@account.command()
@click.argument('name')
def select(name):
    """Select which account to use"""
    pass


@account.command()
@click.argument('name')
def inspect(name):
    """Display the details of an account"""
    pass
