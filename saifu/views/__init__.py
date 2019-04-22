import click

from saifu.views import account
from saifu.views import network
from saifu.views import message

__all__ = ['account', 'network', 'message']

QUESTION_BULLET = f'{click.style("?", fg="cyan")}'
SELECTED_INDICATOR = '*'
