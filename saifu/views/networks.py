import click


def list(accounts):
    DEFAULT = '*'
    for account in accounts:
        click.echo('{} {}'.format(
            DEFAULT if account['default'] else ' ' * len(DEFAULT),
            account['name'],
        ))
