import pytest

from saifu.wallet import Wallet

PKEY = '1234567890123456789012345678901234567890123456789012345678901234'


@pytest.fixture
def wallet():
    wallet = Wallet(pkey=PKEY, endpoint='https://testnet.tomochain.com')
    return wallet


def test_instance(wallet):
    assert isinstance(wallet, Wallet)


def test_balance(wallet):
    assert wallet.balance() == 0
