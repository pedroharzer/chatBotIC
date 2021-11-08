from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from models.perguntas import Perguntas, pergunta_schema, perguntas_schema
from models.respostas import Respostas, resposta_schema, respostas_schema
import pickle, codecs




#Retornar a tabela
def return_table():
    #perguntas = db.session.query(Perguntas,Respostas).filter(Perguntas.id == Respostas.pergunta_id,).all()
    perguntas = db.session.execute('SELECT perguntas.id,perguntas.pergunta,respostas.resposta,respostas.sugestoes FROM perguntas INNER JOIN respostas ON perguntas.id=respostas.pergunta_id;')
    tabela = []
    for row in perguntas:
        rowel = dict(row.items())
        rowel["sugestoes"]= row[3].decode('unicode_escape')
        tabela.append(rowel)
    print(tabela)
    if perguntas:
        return jsonify(tabela), 200

    return jsonify({'message':"nada encontrado",'data':{}}), 404
