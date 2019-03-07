from saifu import __version__
from saifu import main


def test_version():
    assert __version__ == '0.1.0'


def test_entrypoint():
    assert main.entrypoint() is None
