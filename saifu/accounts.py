import os
import json

from saifu import crypto
import click


class AccountManager():
    """docstring for AccountManager."""

    FILE_NAME = 'accounts.json'
    FILE_STRUCTURE = {'default': None, 'accounts': {}}

    def __init__(self, password, app_dir=click.get_app_dir('saifu')):
        self.password = password
        self.app_dir = app_dir
        self.path = os.path.join(self.app_dir, self.FILE_NAME)
        self.accounts = self.FILE_STRUCTURE
        try:
            self._load()
        except FileNotFoundError:
            self._write()

    def _load(self):
        with open(self.path) as f:
            self.accounts = json.load(f)

    def _write(self):
        try:
            with open(self.path, 'w') as f:
                    json.dump(self.accounts, f)
        except FileNotFoundError:
            os.makedirs(self.app_dir)
            with open(self.path, 'w') as f:
                    json.dump(self.accounts, f)

    def new(self, name, pkey):
        payload = crypto.encrypt(self.password, pkey)
        self.accounts['accounts'].update({name: {
            'pkey_cipher': payload['cipher'],
            'salt': payload['salt'],
        }})
        self._write()
