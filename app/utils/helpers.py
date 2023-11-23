#!/usr/bin/python3
""" module for some helper functions
"""
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

HASHER = PasswordHasher()


def hash_password(password: str) -> str:
    """function to hash a password
    Args:
        password (str): password to hash
    """
    pass_hash = HASHER.hash(password)

    return pass_hash


def verify_password(password: str, password_hash: str) -> bool:
    """function to compare hash with a password
    Args:
        password (str): password to compare with hash
        password_hash (str): password hash to check compare
    """
    try:
        HASHER.verify(password_hash, password)
        return True
    except VerifyMismatchError:
        return False
