"""
Regras de negócio e acesso ao banco (sessão + consultas).
Nas rotas só chamamos estas funções e devolvemos JSON — fica mais fácil de explicar.
"""

from datetime import datetime

from sqlalchemy import select

from database import SessionLocal
from models import Aluno, Professor, Turma, Produto, Tipo, TipoAnimal


def listar_professores():
    session = SessionLocal()
    try:
        linhas = session.scalars(select(Professor).order_by(Professor.nome)).all()
        return [p.to_dict() for p in linhas]
    finally:
        session.close()

def listar_produtos():
    session = SessionLocal()
    try:
        linhas = session.scalars(select(Produto).order_by(Produto.nome)).all()
        return [p.to_dict() for p in linhas]
    finally:
        session.close()


def listar_tipos():
    session = SessionLocal()
    try:
        linhas = session.scalars(select(Tipo).order_by(Tipo.nome)).all()
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


def _texto_obrigatorio(valor, campo):
    if valor is None or str(valor).strip() == "":
        raise ValueError(f"O campo '{campo}' é obrigatório.")
    return str(valor).strip()


def _texto_opcional(valor):
    if valor is None:
        return None
    texto = str(valor).strip()
    return texto or None


def cadastrar_professor(dados):
    nome = _texto_obrigatorio(dados.get("nome"), "nome")
    email = _texto_opcional(dados.get("email"))

    session = SessionLocal()
    try:
        professor = Professor(nome=nome, email=email)
        session.add(professor)
        session.commit()
        session.refresh(professor)
        return professor.to_dict()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def cadastrar_turma(dados):
    nome = _texto_obrigatorio(dados.get("nome"), "nome")
    codigo = _texto_obrigatorio(dados.get("codigo"), "codigo")
    professor_id = dados.get("professor_id")
    if not professor_id:
        raise ValueError("O campo 'professor_id' é obrigatório.")

    session = SessionLocal()
    try:
        professor = session.get(Professor, int(professor_id))
        if professor is None:
            raise ValueError(f"Professor {professor_id} não encontrado.")

        turma = Turma(nome=nome, codigo=codigo, professor_id=professor.id)
        session.add(turma)
        session.commit()
        session.refresh(turma)
        return turma.to_dict()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def cadastrar_aluno(dados):
    nome = _texto_obrigatorio(dados.get("nome"), "nome")
    email = _texto_opcional(dados.get("email"))
    endereco = _texto_obrigatorio(dados.get("endereco"), "endereco")
    turma_id = dados.get("turma_id")
    if not turma_id:
        raise ValueError("O campo 'turma_id' é obrigatório.")

    session = SessionLocal()
    try:
        turma = session.get(Turma, int(turma_id))
        if turma is None:
            raise ValueError(f"Turma {turma_id} não encontrada.")

        aluno = Aluno(nome=nome, email=email, turma_id=turma.id, endereco=endereco)
        session.add(aluno)
        session.commit()
        session.refresh(aluno)
        return aluno.to_dict()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def cadastrar_produto(dados):
    nome = _texto_obrigatorio(dados.get("nome"), "nome")
    tipo_id = dados.get("tipo_id") or dados.get("id_tipo")
    if not tipo_id:
        raise ValueError("O campo 'tipo_id' é obrigatório.")
    preco = float(_texto_obrigatorio(dados.get("preco"), "preco"))
    quantidade = int(_texto_obrigatorio(dados.get("quantidade"), "quantidade"))
    descricao = _texto_opcional(dados.get("descricao"))
    imagem = _texto_opcional(dados.get("imagem"))
    disponivel = dados.get("disponivel", True)

    agora = datetime.now()

    session = SessionLocal()
    try:
        tipo = session.get(Tipo, int(tipo_id))
        if tipo is None:
            raise ValueError(f"Tipo {tipo_id} não encontrado.")

        produto = Produto(
            nome=nome,
            id_tipo=tipo.id,
            preco=preco,
            quantidade=quantidade,
            descricao=descricao,
            imagem=imagem,
            disponivel=disponivel,
            created_at=agora,
            updated_at=agora,
        )
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto.to_dict()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def cadastrar_tipo(dados):
    nome = _texto_obrigatorio(dados.get("nome"), "nome")
    session = SessionLocal()
    try:
        tipo = Tipo(
            nome=nome
        )
        session.add(tipo)
        session.commit()
        session.refresh(tipo)
        return tipo.to_dict()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def cadastrar_tipoAnimal(dados):
    nome = _texto_obrigatorio(dados.get("nome"), "nome")
    session = SessionLocal()
    try:
        tipoAnimal = TipoAnimal(
            nome=nome
        )
        session.add(tipoAnimal)
        session.commit()
        session.refresh(tipoAnimal)
        return tipoAnimal.to_dict()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
