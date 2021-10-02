from app import db
from flask import request, jsonify
from models.respostas import Respostas, resposta_schema, respostas_schema
 
#cadastrar respostas
def post_resposta():
    resposta = request.json['resposta']
    sugestoes = request.json['sugestoes']
    id_pergunta = request.json['pergunta_id']

    obj_resposta = Respostas(id_pergunta,resposta,sugestoes)
 
    try:
        db.session.add(obj_resposta)
        db.session.commit()
        result = resposta_schema.dump(obj_resposta)
        return jsonify({'msg' : 'ok', 'data' : result}),201
    except Exception as e:
        print(e)
        return jsonify({'message' : 'ok', 'data' : {}}),500
 
#atualizar respostas
def update_resposta():
    id = request.json['id']
    pergunta_id = request.json['pergunta_id']
    resposta = request.json['resposta']
    sugestoes = request.json['sugestoes']
 
    obj_resposta = Respostas.query.get(id)
 
    if not obj_resposta:
        return jsonify({'message':"Resposta nao existe.",'data':{}}), 404
 
    try:
        obj_resposta.pergunta_id = pergunta_id
        obj_resposta.resposta = resposta
        obj_resposta.sugestoes = sugestoes
        db.session.commit()
        result = resposta_schema.dump(obj_resposta)
        return jsonify({'msg' : 'Resposta atualizada', 'data' : result}),201
    except Exception as e:
        print(e)
        return jsonify({'msg' : 'Error', 'data' : result}),500
 
#pegar UMA resposta
def get_resposta():
    resposta_id = request.json['resposta_id']
    resposta = Respostas.query.get(resposta_id)
 
    if resposta:
        result = resposta_schema.dump(resposta)
        return jsonify({'message':'Resposta encontrada','data':result}), 201
    return jsonify({'message' : 'resposta não encontrada', 'data' : {}}),500
 
#pegar TODAS respostas
def get_all_respostas():
    respostas = Respostas.query.all()
    if respostas:
        result = respostas_schema.dump(respostas)
        return jsonify({'message' : 'Respostas cadastradas', 'data' : result}), 201
    return jsonify({'message' : 'Não existem respostas cadastradas', 'data' : {}}),500
 
#deletar resposta
def del_resposta():
    resposta_id = request.json['resposta_id']
    resposta = Respostas.query.get(resposta_id)
    if not resposta:
        return jsonify({'message' : 'Resposta inexistente!', 'data' : {}}), 404
    try:
        db.session.delete(resposta)
        db.session.commit()
        result = resposta_schema.dump(resposta)
        return jsonify({'message' : 'Resposta deletada!', 'data' : result}), 201
    except Exception as err:
        print(err)
        return jsonify({'message' : 'Algum erro ocorreu!', 'data' : {}}), 500
