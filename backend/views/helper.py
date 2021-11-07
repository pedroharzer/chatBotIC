import datetime
from functools import wraps
from app import app
from flask import request, jsonify, session, render_template
from .users import user_by_username
import jwt
from werkzeug.security import check_password_hash


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = request.authorization
    print(auth)
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Login ou senha inválidos.', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'Usuario nao encontrado.', 'data': []}), 401

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                           app.config['SECRET_KEY'])
        return jsonify({'message': 'Logado com sucesso.', 'token': token.decode('UTF-8'),
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'Login ou senha inválidos.', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401 


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = session['sessiontoken']
        except:
            try:
                headers = request.headers
                bearer = headers.get('Authorization')
                token = bearer.split()[1]
            except:
                #return jsonify({'message': 'Token nao encontrado.', 'data': []}), 403
                return render_template("403.html")
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_by_username(username=data['username'])
        except:
            #return jsonify({'message': 'Token invalido ou expirado.', 'data': []}), 401
            return render_template("403.html")
        return f(current_user, *args, **kwargs)
    return decorated


def savetoken():
    token = request.json['token']
    session['sessiontoken'] = token
    return jsonify({'message': 'Token salvo com sucesso.', 'data': []}), 200

def returnuser():
    try:
        token = session['sessiontoken']
        data = jwt.decode(token, app.config['SECRET_KEY'])
        current_user = data['username']
        return jsonify({'username': current_user}), 200
    except Exception as e:
        return '',403

def logout():
    try:
        session.clear()
        return '', 200
    except Exception as e:
        return '',403