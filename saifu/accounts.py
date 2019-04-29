import os
import json

from eth_account import Account
from saifu import crypto
import click


class AccountsManager():
    """Manage accounts and storing them"""

    FILE_NAME = 'accounts.json'
    FILE_STRUCTURE = {'current': None, 'accounts': {}}

    def __init__(self, app_dir=click.get_app_dir('saifu')):
        self.app_dir = app_dir
        self.path = os.path.join(self.app_dir, self.FILE_NAME)
        self.store = self.FILE_STRUCTURE
        try:
            self._load()
        except FileNotFoundError:
            self._write()

    def _load(self):
        """Load accounts from file"""
        with open(self.path) as f:
            self.store = json.load(f)

    def _write(self):
        """Write accounts to file"""
        try:
            with open(self.path, 'w') as f:
                json.dump(self.store, f)
        except FileNotFoundError:
            os.makedirs(self.app_dir)
            with open(self.path, 'w') as f:
                json.dump(self.store, f)

    def new(self, name, pkey, password):
        """Add a new account"""
        payload = crypto.encrypt(password, pkey)
        account = Account.privateKeyToAccount(pkey)
        self.store['accounts'].update({name: {
            'salt': payload['salt'],
            'pkey_cipher': payload['cipher'],
            'address': account.address,
        }})
        if not self.store['current']:
            self.store['current'] = name
        self._write()

    def list(self):
        """List accounts"""
        accounts = []
        for name, values in self.store['accounts'].items():
            accounts.append({
                'name': name,
                'current': True if self.store['current'] == name else False,
                'address': values['address'],
            })
        return accounts

    def get(self, name, password):
        """Get an account details"""
        return {
            'pkey': crypto.decrypt(
                password,
                self.store['accounts'][name]['salt'],
                self.store['accounts'][name]['pkey_cipher'],
            ),
            'address': self.store['accounts'][name]['address'],
        }

    def rm(self, name):
        """Remove an account"""
        del(self.store['accounts'][name])
        self._write()

    def select(self, name):
        """Set currently selected account"""
        if name not in self.store['accounts'].keys():
            raise KeyError('Not network found with this name')
        else:
            self.store['current'] = name
            self._write()

    def selected(self):
        """Get currently selected account"""
        return self.store['current']
