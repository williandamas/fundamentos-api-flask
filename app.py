from typing import Optional, List
from itertools import count
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

server = Flask(__name__)
spec = FlaskPydanticSpec('Flask', title='Marketing Vough')
spec.register(server)
database = TinyDB(storage=MemoryStorage)
c = count()


class QueryLead(BaseModel):
    id: Optional[int]
    nome: Optional[str]
    idade: Optional[int]


class Lead(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    nome: str
    idade: int


class Leads(BaseModel):
    pessoas: List[Lead]
    count: int


@server.get('/leads')  # rota, endpoint, recurso...
@spec.validate(
    query=QueryLead,
    resp=Response(HTTP_200=Leads)
)
def buscar_pessoas():
    """Retorna todos os leads da base de dados"""
    query = request.context.query.dict(exclude_none=True)
    todos_leads = database.search(
        Query().fragment(query)
    )
    return jsonify(
        Leads(
            pessoas=todos_leads,
            count=len(todos_leads)
        ).dict()
    )


@server.get('/lead/<int:id>')  # rota, endpoint, recurso...
@spec.validate(resp=Response(HTTP_200=Lead))
def buscar_pessoa(id):
    """Retorna o lead por id da base de dados"""
    try:
        pessoa = database.search(Query().id == id)[0]
    except IndexError:
        return {'message': 'Pessoa não encontrada'}, 404
    return jsonify(pessoa)


@server.post('/leads')
@spec.validate(body=Request(Lead), resp=Response(HTTP_201=Lead))
def inserir_pessoa():
    """Insere Lead no banco de Dados"""
    body = request.context.body.dict()
    database.insert(body)
    return body


@server.put('/leads/<int:id>')
@spec.validate(
    body=Request(Lead),
    resp=Response(HTTP_200=Lead)
)
def altera_pessoa(id):
    """Altera Lead do banco de dados"""
    body = request.context.body.dict()
    database.update(body, Query().id == id)
    return jsonify(body)


@server.delete('/leads/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deleta_pessoa(id):
    """Deleta Lead do banco de Dados"""
    database.remove(Query().id == id)
    return jsonify({})


server.run()