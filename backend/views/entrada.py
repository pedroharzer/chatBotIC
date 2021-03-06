from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from models.perguntas import Perguntas, pergunta_schema, perguntas_schema
from models.respostas import Respostas, resposta_schema, respostas_schema
from apis.match_entrada import stringExists
import unidecode
#Cadastrar pergunta
def post_entrada():
    entrada = unidecode.unidecode(request.json['entrada'].lower())
    entrada = ' ' + entrada if not entrada.startswith(' ') else entrada
    perguntas = Perguntas.query.all()
    if perguntas:
        result = perguntas_schema.dump(perguntas)
        for x in result:
            try:
                if(stringExists(x["pergunta"],entrada)):
                    respostas = Respostas.query.all()
                    if respostas:
                        result2 = respostas_schema.dump(respostas)
                        for y in result2:
                            if(y["pergunta_id"]==x["id"]):
                                return jsonify({'resposta':y["resposta"],'sugestoes':y['sugestoes']})
            except:
                pass
    return jsonify({'resposta':'Desculpe, a sua pergunta não foi entendida!'})
                        
