# generate_secret_key.py

import secrets

secret_key = secrets.token_urlsafe(32)

with open('.env', 'a') as env_file:
        env_file.write(f'\nSECRET_KEY="{secret_key}"\n')

        print("Secret key generated and added to .env file.")