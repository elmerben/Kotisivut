from flask import Blueprint, render_template, request, redirect
from .kommentointi import Kommentit
from . import db


sivut = Blueprint("sivut", __name__)

@sivut.route("/")
@sivut.route("/koti")
def koti():
    return render_template("koti.html")

@sivut.route("/tiedot")
def yhteystiedot():
    return render_template("tiedot.html")


@sivut.route("/projektit")
def projektit():
    return render_template("projektit.html")

@sivut.route("/vieraskirja", methods=['GET', 'POST'])
def vieraskirja():
    kaikki_kommentit = Kommentit.query.order_by(Kommentit.paivays.asc()).all()
    return render_template("kirja.html", kommentit=kaikki_kommentit)

@sivut.route("/laheta-kommentti", methods=['GET', 'POST'])
def laheta_kommentti():
    if request.method == 'POST':
        kayttajanimi = request.form['kayttajanimi']
        kommentti = request.form['kommentti']
        uusi_kommentti = Kommentit(kayttajanimi=kayttajanimi, kommentti=kommentti)
        db.session.add(uusi_kommentti)
        db.session.commit()
        return redirect('/vieraskirja')
    kaikki_kommentit = Kommentit.query.order_by(Kommentit.paivays.asc()).all()
    return render_template("kirja.html", kommentit=kaikki_kommentit)
