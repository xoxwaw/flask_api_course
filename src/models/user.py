from src.db import db
from src.models.db_action import DBAction
from src.constants import *


class UserModel(db.Model, DBAction):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(USERNAME_LEN), unique=True)
    hashed_password = db.Column(db.String(HASH_LEN))
    salt = db.Column(db.String(SALT_LEN))

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
