import os
import pytest

from saifu.store import Store

PASSWORD = 'test1234'
KEY = '1f2e88b'


@pytest.fixture
def store(tmpdir):
    store = Store(dir=tmpdir)
    return store


def test_instance(store):
    assert isinstance(store, Store)


def test_init(store):
    os.path.isfile(store.path)


def test_insert(store):
    store.insert({'test': 'value'})
    assert len(store.db.all()) == 1
    assert store.db.all()[0]['test'] == 'value'
