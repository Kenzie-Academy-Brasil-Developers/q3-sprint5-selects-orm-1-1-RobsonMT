from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.grupo_dois_model import GrupoDoisModel


def get_all():
    session: Session = db.session

    grupos = session.query(GrupoDoisModel).all()

    return jsonify(grupos), HTTPStatus.OK


def get_by_limit(limit):
    session: Session = db.session

    grupos = session.query(GrupoDoisModel).limit(limit=limit).all()

    return jsonify(grupos), HTTPStatus.OK


def get_start_by_character(caractere: str):
    session: Session = db.session

    search = "{}%".format(caractere)

    grupos = (
        session.query(GrupoDoisModel).filter(GrupoDoisModel.nome.ilike(search)).all()
    )

    return jsonify(grupos), HTTPStatus.OK


def get_end_by_character(caractere: str):
    session: Session = db.session

    search = "%{}".format(caractere)

    grupos = (
        session.query(GrupoDoisModel).filter(GrupoDoisModel.nome.ilike(search)).all()
    )

    return jsonify(grupos), HTTPStatus.OK


def get_by_age(idade: int):
    session: Session = db.session

    grupos = session.query(GrupoDoisModel).filter_by(idade=idade).all()

    return jsonify(grupos), HTTPStatus.OK


def get_by_id(id: int):
    session: Session = db.session

    grupo = session.query(GrupoDoisModel).get(id)

    if not grupo:
        return {"msg": "id not found."}

    return jsonify(grupo), HTTPStatus.OK
