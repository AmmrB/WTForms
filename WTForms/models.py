# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(500))
    age = db.Column(db.Integer)
    notes = db.Column(db.String(500))
    available = db.Column(db.Boolean, default=True)