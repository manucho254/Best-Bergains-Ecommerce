#!/usr/bin/python3
""" module for some helper functions
"""
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from app.utils.constants import MEDIA_PATH
from app.utils.validations import validate_img_extension

from werkzeug.datastructures import FileStorage

import uuid
import os
from datetime import datetime

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


def process_image(file: FileStorage) -> dict:
    """ Image processing function for uploaded images
        Args:
            file (file object): file object to process
        Returns:
            dict: an empty dict if file is not valid else return path and name of file
    """
    if not validate_img_extension(file.filename):
        return {}

    timestamp = datetime.now().strftime("%d-%m-%Y")
    # rename file using uuid
    new_filename = "{}.{}".format(str(uuid.uuid4()), file.filename.split(".")[-1])

    # check if file path exists
    if not os.path.exists(MEDIA_PATH):
        os.mkdir(MEDIA_PATH)

    current_date_path = os.path.join(MEDIA_PATH, "products", timestamp)
    if not os.path.exists(current_date_path):
        os.mkdir(current_date_path)

    abs_path = os.path.join(current_date_path, new_filename)
    file.save(abs_path)

    # path where file is stored
    # we do the replace for if the code is running on windows system
    path_to_file = os.path.join("products", timestamp, new_filename).replace("\\", "/")

    return {"name": new_filename, "path": path_to_file}
