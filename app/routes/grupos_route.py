from flask import Blueprint

from app.controller import grupo_controller

bp = Blueprint("grupos", __name__, url_prefix="/grupos")

bp.get("")(grupo_controller.get_all)
bp.get("/por_limite/<int:limit>")(grupo_controller.get_by_limit)
bp.get("/inicia_pelo_caractere/<caractere>")(grupo_controller.get_start_by_character)
bp.get("/termina_pelo_caractere/<caractere>")(grupo_controller.get_end_by_character)
bp.get("/por_idade/<int:idade>")(grupo_controller.get_by_age)
bp.get("/pelo_id/<int:id>")(grupo_controller.get_by_id)
