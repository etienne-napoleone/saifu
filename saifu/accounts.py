import os
import json

from saifu import crypto
import click


class AccountsManager():
    """Manage accounts and storing them"""

    FILE_NAME = 'accounts.json'
    FILE_STRUCTURE = {'current': None, 'accounts': {}}

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
        """Load accounts from file"""
        with open(self.path) as f:
            self.accounts = json.load(f)

    def _write(self):
        """Write accounts to file"""
        try:
            with open(self.path, 'w') as f:
                json.dump(self.accounts, f)
        except FileNotFoundError:
            os.makedirs(self.app_dir)
            with open(self.path, 'w') as f:
                json.dump(self.accounts, f)

    def new(self, name, pkey):
        """Add a new account"""
        payload = crypto.encrypt(self.password, pkey)
        self.accounts['accounts'].update({name: {
            'pkey_cipher': payload['cipher'],
            'salt': payload['salt'],
        }})
        if not self.accounts['current']:
            self.accounts['current'] = name
        self._write()

    def list(self):
        """List accounts"""
        accounts = []
        for name, _ in self.accounts['accounts'].items():
            accounts.append({
                'name': name,
                'current': True if self.accounts['current'] == name else False
            })
        return accounts

    def get(self, name):
        """Get an account details"""
        return {'pkey': crypto.decrypt(
            self.password,
            self.accounts['accounts'][name]['salt'],
            self.accounts['accounts'][name]['pkey_cipher']
        )}

    def rm(self, name):
        """Remove an account"""
        del(self.accounts['accounts'][name])
        self._write()
