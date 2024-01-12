from flask_login import UserMixin
from . import db
from sqlalchemy import Enum

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))
    user_role = db.Column(Enum('admin', 'user'), default='user')
    bio = db.Column(db.Text)
    profile_pic = db.Column(db.String(255))


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    instructions = db.Column(db.Text, nullable=False)
    servings = db.Column(db.Integer)
    prep_time = db.Column(db.Integer)  # in minutes
    cook_time = db.Column(db.Integer)  # in minutes
    total_time = db.Column(db.Integer)  # in minutes
    created_at = db.Column(db.TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = db.Column(
        db.TIMESTAMP, server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
    )