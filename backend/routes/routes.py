from app import app
from flask import jsonify, render_template
from views import users, helper, perguntas, entrada, respostas, table

#Cadastro do usuário
@app.route('/user', methods=['POST'])
def post_user():
    return users.post_user()

#Login do usuário
@app.route('/login', methods=['POST'])
def authenticate():
    return helper.auth()

#Atualizar os dados do usuário. É necessário fornecer o JSON com os dados. O usuário precisa estar logado (bearer token fornecido)
@app.route('/user', methods=['PUT'])
@helper.token_required
def update_self(current_user):
    return users.update_user(current_user.id)

#Apagar o cadastro do usuário logado. O usuário precisa estar logado (bearer token fornecido)
@app.route('/user', methods=['DELETE'])
@helper.token_required
def delete_self(current_user):
    return users.delete_user(current_user.id)

#Recebe pergunta de usuário
@app.route('/entrada', methods=['POST'])
def post_entrada():
    return entrada.post_entrada()

#Cadastro de pergunta pelo admin
@app.route('/pergunta', methods=['POST'])
def post_pergunta():
    return perguntas.post_pergunta()

@app.route('/resposta', methods=['POST'])
def post_resposta():
    return respostas.post_resposta()
 
#Update resposta
@app.route('/resposta', methods=['PUT'])
def update_resposta():
    return respostas.update_resposta()
 
#Coletar UMA resposta
@app.route('/resposta/<int:id>', methods=['GET'])
def get_resposta(id):
    return respostas.get_resposta(id)
 
#Coletar TODAS as respostas
@app.route('/respostas', methods=['GET'])
def get_all_resposta():
    return respostas.get_all_respostas()
 
@app.route('/resposta', methods=['DELETE'])
def delete_resposta():
    return respostas.del_resposta()

@app.route('/pergunta', methods=['DELETE'])
def delete_pergunta():
    return perguntas.delete_pergunta()

@app.route('/perguntas', methods=['GET'])
def get_all_perguntas():
    return perguntas.get_perguntas()

@app.route('/pergunta/get', methods=['GET'])
def get_pergunta():
    return perguntas.get_pergunta()

@app.route('/pergunta', methods=['PUT'])
def update_pergunta():
    return perguntas.update_pergunta()

@app.route('/tabela', methods=['GET'])
def return_table():
    return table.return_table()

@app.route('/cadastropergunta')
@helper.token_required
def cadastro_pergunta(current_user):
    return render_template("cadastropergunta.html")

@app.route('/userlogado', methods=['GET'])
def userlogado():
    return helper.returnuser()

@app.route('/cadastrousuario')
def cadastro_usuario():
    return render_template("cadastrousuario.html")

@app.route('/loginusuario')
def login_user():
    return render_template("loginusuario.html")

@app.route('/logout')
def logout():
    helper.logout()
    return render_template("index.html")

@app.route('/savetoken', methods=['POST'])
def savetoken():
    return helper.savetoken()


@app.route("/")
def home():
    return render_template("index.html")