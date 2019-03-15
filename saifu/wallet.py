from web3 import Web3, HTTPProvider
from eth_account import Account


class Wallet:
    """Class representing a wallet
    Interact with the blockchain
    """

    def __init__(self, pkey, endpoint='https://rpc.tomochain.com'):
        self.pkey = pkey
        self.endpoint = endpoint
        self.web3 = Web3(HTTPProvider(self.endpoint))
        self.account = Account.privateKeyToAccount(pkey)

    def balance(self):
        "Get the wallet balance"
        return self.web3.fromWei(
            self.web3.eth.getBalance(self.account.address),
            'ether'
        )
