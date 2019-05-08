import click


# from saifu import views
def balance(amount, ticker):
    """View for displaying account balance"""
    click.echo('{:.4f} {}'.format(
        amount,
        click.style(ticker, fg='yellow'),
    ))
