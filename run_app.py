#!/usr/bin/python3
""" module to run flask application """

from config import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
