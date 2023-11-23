#!/usr/bin/python3
""" module to get environment variable
"""

from os import getenv

# get db environment variables
DB_USER = getenv("DB_USER")
DB_PWD = getenv("DB_PWD ")
DB_HOST = getenv("DB_HOST")
DB_NAME = getenv("DB_NAME")

# mysql db uri
DB_URI = "mysql://{}:{}@{}/{}".format(DB_USER, DB_PWD, DB_HOST, DB_NAME)
