import click

from saifu.views import account
from saifu.views import balance
from saifu.views import message
from saifu.views import network

__all__ = ['account', 'balance', 'message', 'network']

QUESTION_BULLET = f'{click.style("?", fg="cyan")}'
SELECTED_INDICATOR = '•'
