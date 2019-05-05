import click

from saifu.accounts import AccountsManager
from saifu import views
import cryptography

a = AccountsManager()


@click.group()
def account():
    """Manage the different accounts saifu can use"""
    pass


@account.command()
def ls():
    """List all available accounts"""
    accounts = a.list()
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
    try:
        a.add(name, pkey, password)
        views.account.add(name)
    except ValueError:
        views.message.error(f'The private key is not valid')


@account.command()
@click.argument('name')
def rm(name):
    """Remove an account"""
    try:
        a.rm(name)
        views.account.rm(name)
    except KeyError:
        views.message.error(f'No account found with name {name}')


@account.command()
@click.argument('name')
def select(name):
    """Select which account to use"""
    try:
        a.select(name)
        views.account.select(name)
    except KeyError:
        views.message.error(f'No account found with name {name}')


@account.command()
@click.argument('name')
@click.option('--password', prompt=f'{views.QUESTION_BULLET} Password', hide_input=True)  # noqa: E501
@click.option('--export', is_flag=True)
def inspect(name, password, export):
    """Display the details of an account"""
    if export:
        export = click.confirm(
            f'{views.QUESTION_BULLET} Are you sure you want to '
            'expose the private key?'
        )
    try:
        views.account.inspect(name, export, **a.inspect(name, password))
    except KeyError:
        views.message.error(f'No account found with name {name}')
    except cryptography.fernet.InvalidToken:
        views.message.error(f'Invalid password')
