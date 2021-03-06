import os
import json

from web3 import Web3, HTTPProvider
import click


class NetworksManager():
    """Manage networks and storing them"""

    FILE_NAME = 'networks.json'
    FILE_STRUCTURE = {
        'current': 'mainnet',
        'networks': {
            'mainnet': {
                'rpc_url': 'https://rpc.tomochain.com',
                'chain_id': '88',
                'ticker': 'TOMO',
            },
            'testnet': {
                'rpc_url': 'https://testnet.tomochain.com',
                'chain_id': '89',
                'ticker': 'TOMO',
            },
        }
    }

    def __init__(self, app_dir=click.get_app_dir('saifu')):
        self.app_dir = app_dir
        self.path = os.path.join(self.app_dir, self.FILE_NAME)
        self.store = self.FILE_STRUCTURE
        try:
            self._load()
        except FileNotFoundError:
            self._write()

    def _load(self):
        """Load networks from file"""
        with open(self.path) as f:
            self.store = json.load(f)

    def _write(self):
        """Write networks to file"""
        try:
            with open(self.path, 'w') as f:
                json.dump(self.store, f)
        except FileNotFoundError:
            os.makedirs(self.app_dir)
            with open(self.path, 'w') as f:
                json.dump(self.store, f)

    def add(self, name, rpc_url, chain_id, ticker):
        """Add a new network"""
        self.store['networks'].update({name: {
            'rpc_url': rpc_url,
            'chain_id': chain_id,
            'ticker': ticker,
        }})
        self._write()

    def list(self):
        """List networks"""
        networks = []
        for name, _ in self.store['networks'].items():
            networks.append({
                'name': name,
                'current': True if self.selected() == name else False
            })
        return networks

    def inspect(self, name):
        """Get a network details"""
        return self.store['networks'][name]

    def get(self, name):
        """Get a network object"""
        endpoint = self.store['networks'][name]['rpc_url']
        return Web3(HTTPProvider(endpoint))

    def rm(self, name):
        """Remove a network"""
        del(self.store['networks'][name])
        self._write()

    def select(self, name):
        """Set currently selected network"""
        if name not in self.store['networks'].keys():
            raise KeyError('No network found with this name')
        else:
            self.store['current'] = name
            self._write()

    def selected(self):
        """Get currently selected network"""
        return self.store['current']
