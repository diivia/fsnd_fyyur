import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Suppress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database


# TODO: DONE: IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://julijakondratjeva@localhost:5432/fyyur'
