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

SECRET_KEY =  getenv("SECRET_KEY")

SECRET_KEY = "$argon2id$v=19$m=65536,t=3,p=4$iTrh7N9bQJMu/Fg9KPIHrg$RzR/ZvHEttvpSNuXPB3+TR5Y+BAkRQh28xsjdanslmc"
DB_URI = "mysql://root:#Re$ds%Fio02H$@localhost:3306/best_bargains"