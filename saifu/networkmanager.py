from saifu.network import Network


class NetworkManager():
    """NetworkManager that interface to all networks"""

    default_networks = [
        Network(
            88,
            'TomoChain mainnet',
            'https://rpc.tomochain.com',
            'TOMO',
        ),
        Network(
            89,
            'TomoChain testnet',
            'https://testnet.tomochain.com',
            'TOMO',
        ),
        Network(
            90,
            'TomoChain devnet',
            'https://rpc.devnet.tomochain.com',
            'TOMO',
        ),
    ]

    def __init__(self, store):
        self.store = store
        self.custom_networks = []
        for result in self.store.db.search(self.store.key.network):
            self.custom_networks.append(Network(
                result['network']['id'],
                result['network']['name'],
                result['network']['rpc'],
                result['network']['ticker'],
            ))

    def add(self, id, name, rpc, ticker):
        """add a new network"""
        return self.store.db.insert({'network': {
            'id': id,
            'name': name,
            'rpc': rpc,
            'ticker': ticker,
        }})
        self.custom_networks += [Network(id, name, rpc, ticker)]

    def remove(self, id):
        """remove a network"""
        if [network for network in self.default_networks if network.id == id]:
            raise IndexError('You can not delete a default network')
        else:
            # Remove from db doesn't work
            # https://github.com/msiemens/tinydb/issues/261
            self.store.db.remove(self.store.key.networks.id == id)
            for index, network in enumerate(self.custom_networks):
                if id == network.id:
                    self.custom_networks.pop(index)

    def all(self):
        """return all networks"""
        return self.default_networks + self.custom_networks
