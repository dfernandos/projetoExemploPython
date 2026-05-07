import flask as fk

from servicos import listar_alunos, listar_professores, listar_turmas

bp = fk.Blueprint("api", __name__, url_prefix="/api")


@bp.get("/professores")
def professores():
    # A rota só liga a URL ao serviço e transforma o resultado em JSON.
    return fk.jsonify(listar_professores())


@bp.get("/turmas")
def turmas():
    return fk.jsonify(listar_turmas())


@bp.get("/alunos")
def alunos():
    return fk.jsonify(listar_alunos())
