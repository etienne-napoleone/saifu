import base64
import os
import pickle

import click
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KeyStore:
    """Class representing a keystore
    Store a dict of keys
    """

    def __init__(self, password):
        self.dir = click.get_app_dir('saifu')
        self.store_path = os.path.join(self.dir, 'keystore')
        self.salt_path = os.path.join(self.dir, 'salt')
        self.password = password
        self.store = None
        self.fernet = None

    def load(self):
        """Load existing salt and keystore"""
        with open(self.salt_path, 'rb') as f:
            salt = pickle.load(f)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.fernet = Fernet(
            base64.urlsafe_b64encode(kdf.derive(str.encode(self.password)))
        )
        with open(self.store_path, 'rb') as f:
            self.store = pickle.loads(self.fernet.decrypt(f.read()))

    def init(self):
        """Init a new salt and keystore"""
        os.makedirs(self.dir, exist_ok=True)
        salt = os.urandom(16)
        with open(self.salt_path, 'wb+') as f:
            pickle.dump(salt, f)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.fernet = Fernet(
            base64.urlsafe_b64encode(kdf.derive(str.encode(self.password)))
        )
        with open(self.store_path, 'wb+') as f:
            store = {}
            f.write(self.fernet.encrypt(pickle.dumps(store)))
            self.store = store

    def add(self, name, pkey):
        """Add or update a key in the keystore"""
        self.store[name] = pkey
        with open(self.store_path, 'wb+') as f:
            f.write(self.fernet.encrypt(pickle.dumps(self.store)))

    def rm(self, name):
        """Delete a key in the keystore"""
        del(self.store[name])
        with open(self.store_path, 'wb+') as f:
            f.write(self.fernet.encrypt(pickle.dumps(self.store)))
