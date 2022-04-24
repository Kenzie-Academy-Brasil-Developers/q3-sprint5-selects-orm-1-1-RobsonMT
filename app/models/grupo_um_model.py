from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from app.configs.database import db


@dataclass
class GrupoUmModel(db.Model):
    # id: int
    nome: int
    # idade: int
    __tablename__ = "grupo_um"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
