import click


def error(message):
    click.echo('{} {}'.format(
        click.style('!', fg='red'),
        message,
    ))
