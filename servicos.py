"""
Regras de negócio e acesso ao banco (sessão + consultas).
Nas rotas só chamamos estas funções e devolvemos JSON — fica mais fácil de explicar.
"""

from sqlalchemy import select

from database import SessionLocal
from models import Aluno, Professor, Turma


def listar_professores():
    session = SessionLocal()
    try:
        linhas = session.scalars(select(Professor).order_by(Professor.nome)).all()
        return [p.to_dict() for p in linhas]
    finally:
        session.close()


def listar_turmas():
    session = SessionLocal()
    try:
        linhas = session.scalars(select(Turma).order_by(Turma.codigo)).all()
        return [t.to_dict() for t in linhas]
    finally:
        session.close()


def listar_alunos():
    session = SessionLocal()
    try:
        linhas = session.scalars(select(Aluno).order_by(Aluno.nome)).all()
        return [a.to_dict() for a in linhas]
    finally:
        session.close()
