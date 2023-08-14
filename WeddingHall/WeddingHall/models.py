from flask_sqlalchemy import SQLAlchemy
from WeddingHall import app
from WeddingHall import db

class AdminPanel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    guest = db.Column(db.Integer, nullable=False)
    hall = db.Column(db.String(50), nullable=False)
