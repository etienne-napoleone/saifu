import os
import pickle
import pytest

from cryptography.fernet import Fernet

from saifu.keystore import KeyStore

PASSWORD = 'test1234'
KEY = '1f2e88b'


@pytest.fixture
def keystore(tmpdir):
    keystore = KeyStore(PASSWORD)
    keystore.dir = tmpdir
    keystore.path = os.path.join(keystore.dir, 'keystore')
    keystore.salt_path = os.path.join(keystore.dir, 'salt')
    return keystore


def test_instance(keystore):
    assert isinstance(keystore, KeyStore)


def test_init(keystore):
    keystore.init()
    assert keystore.store == {}
    assert isinstance(keystore.fernet, Fernet)
    with open(keystore.salt_path, 'rb') as f:
        assert isinstance(pickle.load(f), bytes)
    with open(keystore.store_path, 'rb') as f:
        assert isinstance(
            pickle.loads(keystore.fernet.decrypt(f.read())), dict
        )


def test_load(keystore):
    keystore2 = keystore
    keystore.init()
    keystore2.load()
    assert keystore2.store == {}
    assert isinstance(keystore2.fernet, Fernet)


def test_add(keystore):
    keystore.init()
    keystore.add('default', KEY)
    assert keystore.store['default'] == KEY


def test_rm(keystore):
    keystore.init()
    keystore.add('default', KEY)
    keystore.rm('default')
    with pytest.raises(KeyError):
        assert keystore.store['default']
