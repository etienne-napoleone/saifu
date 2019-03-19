import os

import click
import tinydb


class Store:
    """Class representing a store"""

    def __init__(self):
        self.app_dir = click.get_app_dir('saifu')
        self.store_path = os.path.join(self.app_dir, 'store.json')
        try:
            self.db = tinydb.TinyDB(self.store_path)
        except FileNotFoundError:
            os.makedirs(self.app_dir)
            self.db = tinydb.TinyDB(self.store_path)
        self.key = tinydb.Query()

    def insert(self, data):
        """Insert an item in the store"""
        return self.db.insert(data)

    def update(self, data, query):
        """Update an item in the store"""
        return self.db.update(data, query)

    def remove(self, query):
        """Remove an item in the store"""
        return self.db.remove(query)

    def search(self, query):
        """Search items in the store"""
        return self.db.search(query)

    def all(self):
        """Get all items from store"""
        return self.db.all()

    def purge(self):
        """Empty the store"""
        return self.db.purge()
