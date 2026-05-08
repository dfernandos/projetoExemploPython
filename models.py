from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=True)

    turmas = relationship("Turma", back_populates="professor")

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}

    def __repr__(self):
        return f"<Professor {self.id} {self.nome!r}>"


class Turma(Base):
    __tablename__ = "turmas"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    codigo = Column(String(40), unique=True, nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.id"), nullable=False)

    professor = relationship("Professor", back_populates="turmas")
    alunos = relationship("Aluno", back_populates="turma")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "codigo": self.codigo,
            "professor_id": self.professor_id,
        }

    def __repr__(self):
        return f"<Turma {self.id} {self.codigo!r}>"


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=True)
    turma_id = Column(Integer, ForeignKey("turmas.id"), nullable=False)
    endereco = Column(String(120), nullable=False)


    turma = relationship("Turma", back_populates="alunos")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "turma_id": self.turma_id,
            "endereco": self.endereco
        }

    def __repr__(self):
        return f"<Aluno {self.id} {self.nome!r} {self.endereco!r}>"


class Tipo(Base):
    __tablename__ = "tipos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)

    produtos = relationship("Produto", back_populates="tipo")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }

    def __repr__(self):
        return f"<Tipo {self.id} {self.nome!r}>"


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    preco = Column(Float(precision=2), nullable=False)
    quantidade = Column(Integer, nullable=False)
    descricao = Column(String(120), nullable=True)
    imagem = Column(String(120), nullable=True)
    disponivel = Column(Boolean, default=True)
    id_tipo = Column(Integer, ForeignKey("tipos.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    tipo = relationship("Tipo", back_populates="produtos")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "id_tipo": self.id_tipo,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "descricao": self.descricao,
            "imagem": self.imagem,
            "disponivel": self.disponivel,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self):
        return f"<Produto {self.id} {self.nome!r}>"


class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=True)
    senha = Column(String(120), nullable=False)
    id_departamento = Column(Integer, ForeignKey("departamentos.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    departamento = relationship("Departamento", back_populates="funcionarios")


    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "id_departamento": self.id_departamento,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self):
        return f"<Funcionario {self.id} {self.nome!r}>" 


class Departamento(Base):
    __tablename__ = "departamentos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="departamento")


    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }

    def __repr__(self):
        return f"<Departamento {self.id} {self.nome!r}>"



########

class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    id_tipo_animal = Column(Integer, ForeignKey("tipo_animal.id"), nullable=False)

    tipo_animal = relationship("TipoAnimal", back_populates="animais")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "id_tipo_animal": self.id_tipo_animal,
            "created": self.created_at
        }

    def __repr__(self):
        return f"<Animal {self.id} {self.nome!r}>"



class TipoAnimal(Base):
    __tablename__ = "tipo_animal"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)

    animais = relationship("Animal", back_populates="tipo_animal")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

    def __repr__(self):
        return f"<TipoAnimal {self.id} {self.nome!r}>"

