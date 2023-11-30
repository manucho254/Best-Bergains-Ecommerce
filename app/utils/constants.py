#!/usr/bin/python3

import os

USER_FIELDS = ["email", "username", "first_name", "last_name"]
ADDRESS_FIELDS = ["country", "city", "phone", "address_line_1", "address_line_2", "zip_code"]
PRODUCT_FIELDS = ["title", "description", "price"]
PRODUCT_IMAGE_FIELDS = ["name", "file_path"]
MEDIA_PATH = os.path.join("app", "media")