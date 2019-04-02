import os
import pytest

from saifu.store import Store

TEST_VALUE = {'test': 'value'}


@pytest.fixture
def store(tmpdir):
    store = Store(dir=tmpdir)
    return store


def test_instance(store):
    assert isinstance(store, Store)


def test_init(store):
    assert os.path.isfile(store.path)


def test_init_existing(store):
    os.remove(store.path)
    os.rmdir(store.dir)
    store_2 = Store(dir=store.dir)
    assert os.path.isfile(store_2.path)


def test_insert(store):
    store.db.insert(TEST_VALUE)
    assert len(store.db.all()) == 1
    assert store.db.all()[0]['test'] == TEST_VALUE['test']
