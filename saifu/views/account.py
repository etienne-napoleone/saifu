import click

from saifu import views


def list(accounts):
    for account in accounts:
        click.echo('{} {}'.format(
            views.SELECTED_INDICATOR if account['current']
            else ' ' * len(views.SELECTED_INDICATOR),
            account['name'],
        ))


def add(name):
    click.echo('Added account {}'.format(click.style(name, fg='green')))


def rm(name):
    click.echo('Removed account {}'.format(click.style(name, fg='green')))


def select(name):
    click.echo('Selected account {}'.format(click.style(name, fg='green')))

# def inspect(name, rpc_url, chain_id, ticker):
#     el = '  {} {}'.format('{}:', click.style('{}', fg='yellow'))
#     click.echo(el.format('RPC url', rpc_url))
#     click.echo(el.format('Chain id', chain_id))
#     click.echo(el.format('Ticker', ticker))
