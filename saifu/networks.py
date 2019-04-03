import os
import json

import click


class NetworksManager():
    """Manage networks and storing them"""

    FILE_NAME = 'networks.json'
    FILE_STRUCTURE = {
        'current': 'TomoChain',
        'networks': {
            'TomoChain': {
                'rpc_url': 'https://rpc.tomochain.com',
                'chain_id': '88',
                'ticker': 'TOMO',
            },
            'TomoChain testnet': {
                'rpc_url': 'https://testnet.tomochain.com',
                'chain_id': '89',
                'ticker': 'TOMO',
            },
        }
    }

    def __init__(self, app_dir=click.get_app_dir('saifu')):
        self.app_dir = app_dir
        self.path = os.path.join(self.app_dir, self.FILE_NAME)
        self.networks = self.FILE_STRUCTURE
        try:
            self._load()
        except FileNotFoundError:
            self._write()

    def _load(self):
        """Load networks from file"""
        with open(self.path) as f:
            self.networks = json.load(f)

    def _write(self):
        """Write networks to file"""
        try:
            with open(self.path, 'w') as f:
                json.dump(self.networks, f)
        except FileNotFoundError:
            os.makedirs(self.app_dir)
            with open(self.path, 'w') as f:
                json.dump(self.networks, f)

    def new(self, name, rpc_url, chain_id, ticker):
        """Add a new network"""
        self.networks['networks'].update({name: {
            'rpc_url': rpc_url,
            'chain_id': chain_id,
            'ticker': ticker,
        }})
        self._write()

    def list(self):
        """List networks"""
        networks = []
        for name, _ in self.networks['networks'].items():
            networks.append({
                'name': name,
                'current': True if self.networks['current'] == name else False
            })
        return networks

    def get(self, name):
        """Get an network details"""
        return self.networks['networks'][name]

    def rm(self, name):
        """Remove a network"""
        del(self.networks['networks'][name])
        self._write()
