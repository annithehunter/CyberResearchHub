from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(50),
        unique=True
    )

    email = db.Column(
        db.String(120),
        unique=True
    )

    password_hash = db.Column(
        db.String(255)
    )

    role = db.Column(
        db.String(20),
        default="user"
    )
