#!/usr/bin/python3
""" module to store all constant variables
"""

import os

USER_MODEL_FIELDS = ["email", "username", "first_name", "last_name"]
ADDRESS_MODEL_FIELDS = ["country", "city", "phone", "address_line_1", "address_line_2", "zip_code"]
PRODUCT_MODEL_FIELDS = ["title", "description", "price"]
MEDIA_PATH = os.path.join("app", "media")