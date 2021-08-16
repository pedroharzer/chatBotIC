import datetime
from app import db, ma

#Definição da classe / tabela usuário e seus campos

class Perguntas(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    pergunta = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self,pergunta):
        self.pergunta = pergunta

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class PerguntasSchema(ma.Schema):
    class Meta:
        fields = ('id','pergunta','created_on')

pergunta_schema = PerguntasSchema()
perguntas_schema = PerguntasSchema(many=True)

db.create_all()
db.session.commit()