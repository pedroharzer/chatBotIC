from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.perguntas import Perguntas, pergunta_schema, perguntas_schema

#Cadastrar pergunta
def post_pergunta():
    pergunta = request.json['pergunta']
    objpergunta = Perguntas(pergunta)
    try:
        db.session.add(objpergunta)
        db.session.commit()
        result = pergunta_schema.dump(objpergunta)
        return jsonify({'message':'Pergunta cadastrada com sucesso', 'data': result}),201
    except Exception as e:
        print(e)
        return jsonify({'message':'Erro ao cadastrar pergunta.','data':{}}),500

#Atualizar/editar pergunta
def update_pergunta(id):
    pergunta = request.json['pergunta']
    
    objpergunta = Perguntas.query.get(id)

    if not objpergunta:
        return jsonify({'message':"Pergunta nao existe.",'data':{}}), 404


    try:
        objpergunta.pergunta = pergunta
        db.session.commit()
        result = pergunta_schema.dump(pergunta)
        return jsonify({'message':'Pergunta atualizada com sucesso.', 'data': result}),201
    except Exception as e:
        print(e)
        return jsonify({'message':'Erro ao atualizar pergunta.','data':{}}),500

#Coletar dados da pergunta
def get_pergunta(id):
    pergunta = Perguntas.query.get(id)
    if pergunta:
        result = pergunta_schema.dump(pergunta)
        return jsonify({'message':'succesfully fetched','data':result}), 201

    return jsonify({'message':"pergunta nao existe",'data':{}}), 404


#Coletar TODAS as perguntas
def get_perguntas():
    perguntas = Perguntas.query.all()
    if perguntas:
        result = perguntas_schema.dump(perguntas)
        return jsonify({'message':'succesfully fetched','data':result}), 201

    return jsonify({'message':"nada encontrado",'data':{}}), 404

#Deletar a pergunta
def delete_user(id):
    pergunta = Perguntas.query.get(id)
    if not pergunta:
        return jsonify({'message':"Pergunta nao existe.",'data':{}}),404
    if pergunta:
        try:
            db.session.delete(pergunta)
            db.session.commit()
            result = pergunta_schema.dump(pergunta)
            return jsonify({'message':'Pergunta deletada com sucesso.','data':result}), 200
        except:
            return jsonify({'message':'Erro ao deletar a pergunta.','data':{}}),500