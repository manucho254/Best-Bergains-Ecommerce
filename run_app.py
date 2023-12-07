#!/usr/bin/python3

from config import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(port='5000', host="0.0.0.0")
