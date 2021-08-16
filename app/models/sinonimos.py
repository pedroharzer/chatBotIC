import datetime
from app import db, ma

#Definição da classe / tabela usuário e seus campos

class Sinonimos(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    texto = db.Column(db.String(200), nullable=False)
    sinonimo = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self,texto,sinonimo):
        self.texto = texto
        self.sinonimo = sinonimo

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class SinonimosSchema(ma.Schema):
    class Meta:
        fields = ('id','texto','sinonimo','created_on')

sinonimo_schema = SinonimosSchema()
sinonimos_schema = SinonimosSchema(many=True)

db.create_all()
db.session.commit()