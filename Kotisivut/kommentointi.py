from . import db
from sqlalchemy.sql import func

class Kommentit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kayttajanimi = db.Column(db.String(150), nullable=False)
    kommentti = db.Column(db.Text, nullable=False)
    paivays = db.Column(db.DateTime(timezone=True), default=func.now())


