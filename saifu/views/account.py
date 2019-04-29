import click

from saifu import views


def list(accounts):
    for account in accounts:
        click.echo('{} {} {}'.format(
            views.SELECTED_INDICATOR if account['current']
            else ' ' * len(views.SELECTED_INDICATOR),
            account['name'],
            click.style(account['address'][:7], fg='green'),
        ))


def add(name):
    click.echo('Added account {}'.format(click.style(name, fg='green')))


def rm(name):
    click.echo('Removed account {}'.format(click.style(name, fg='green')))


def select(name):
    click.echo(
        'Account {} is now active'.format(click.style(name, fg='green'))
    )


def inspect(name, export, pkey, address):
    el = '  {} {}'.format('{}:', click.style('{}', fg='yellow'))
    click.echo(el.format('Address', address))
    click.echo(el.format('Private key', pkey if export else '******'))
