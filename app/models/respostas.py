import datetime
from app import db, ma

#Definição da classe / tabela usuário e seus campos

class Respostas(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    pergunta_id = db.Column(db.Integer, nullable=False)
    resposta = db.Column(db.String(200), nullable=False)
    sugestoes = db.Column(db.PickleType)
    created_on = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self,pergunta_id,resposta,sugestoes):
        self.pergunta_id = pergunta_id
        self.resposta = resposta
        self.sugestoes = sugestoes

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class RespostasSchema(ma.Schema):
    class Meta:
        fields = ('id','pergunta_id','resposta','sugestoes','created_on')

resposta_schema = RespostasSchema()
respostas_schema = RespostasSchema(many=True)

db.create_all()
db.session.commit()
