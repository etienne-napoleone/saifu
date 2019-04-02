import os

import click
import tinydb


class Store:
    """Class representing a store"""

    def __init__(self, dir=click.get_app_dir('saifu')):
        self.dir = dir
        self.path = os.path.join(self.dir, 'store.json')
        try:
            self.db = tinydb.TinyDB(self.path)
        except FileNotFoundError:
            os.makedirs(self.dir)
            self.db = tinydb.TinyDB(self.path)
        self.key = tinydb.Query()
