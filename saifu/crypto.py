import base64
import uuid

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(password, plain):
    """Encrypt data with given salt and password"""
    salt = uuid.uuid4().hex.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    fernet = Fernet(
        base64.urlsafe_b64encode(kdf.derive(str.encode(password)))
    )
    return {
        'salt': salt.decode('utf-8'),
        'cipher': fernet.encrypt(plain.encode('utf-8')).decode('utf-8'),
    }
