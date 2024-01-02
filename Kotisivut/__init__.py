from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
KANTA_NIMI = "database.db"


def sovellus():
    paasovellus = Flask(__name__)
    paasovellus.config["SALAUSAVAIN"] = "*SALAINEN*"
    paasovellus.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{KANTA_NIMI}'
    db.init_app(paasovellus)

    from .sivut import sivut
    from.kommentointi import Kommentit
    luo_tietokanta(paasovellus)

    paasovellus.register_blueprint(sivut, url_prefix="/")
    
    return paasovellus


def luo_tietokanta(paasovellus):
    if not path.exists("Kotisivut/" + KANTA_NIMI):
        with paasovellus.app_context():
            db.create_all()
        print("Tietokanta luotu.")
