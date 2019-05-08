import click

from saifu import views


def list(networks):
    for network in networks:
        click.echo('{} {}'.format(
            views.SELECTED_INDICATOR if network['current']
            else ' ' * len(views.SELECTED_INDICATOR),
            network['name'],
        ))


def add(name, rpc_url, chain_id, ticker):
    el = '  {} {}'.format('{}:', click.style('{}', fg='yellow'))
    click.echo('Added network {}'.format(click.style(name, fg='green')))
    click.echo(el.format('RPC url', rpc_url))
    click.echo(el.format('Chain id', chain_id))
    click.echo(el.format('Ticker', ticker))


def rm(name):
    click.echo('Removed network {}'.format(click.style(name, fg='green')))


def select(name):
    click.echo('Selected network {}'.format(click.style(name, fg='green')))


def inspect(name, rpc_url, chain_id, ticker):
    el = '{} {}'.format('{}:', click.style('{}', fg='yellow'))
    click.echo(el.format('RPC url', rpc_url))
    click.echo(el.format('Chain id', chain_id))
    click.echo(el.format('Ticker', ticker))
