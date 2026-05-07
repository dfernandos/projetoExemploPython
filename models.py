from sqlalchemy import Column, ForeignKey, Integer, String
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

    turma = relationship("Turma", back_populates="alunos")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "turma_id": self.turma_id,
        }

    def __repr__(self):
        return f"<Aluno {self.id} {self.nome!r}>"
