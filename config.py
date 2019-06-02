import os

class Config():

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgres://postgres:projeto_ds3@localhost:5432/projeto_ds3'
    )

