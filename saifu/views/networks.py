import click


def list(accounts):
    CURRENT = '*'
    for account in accounts:
        click.echo('{} {}'.format(
            CURRENT if account['current'] else ' ' * len(CURRENT),
            account['name'],
        ))
