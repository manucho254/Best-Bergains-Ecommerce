#!/usr/bin/python3

import re

pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


def validate_email(email: str) -> bool:
    """Check if email is valid
    Args:
        email (str): email to validate

    Returns: True if the pattern matches else false
    """
    if re.match(pattern, email):
        return True
    else:
        return False


def validate_extension(file_name: str) -> bool:
    """
    Args:
        file_name (str): name of file to check
    Returns:
        Return true if right extension else false
    """
    valid = ["jpg", "png", "jpeg"]

    if file_name is None:
        return False

    name_split = file_name.split(".")

    return name_split[-1] in valid
