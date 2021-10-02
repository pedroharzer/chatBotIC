import datetime
from app import db, ma

#Definição da classe / tabela usuário e seus campos

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self,username,password):
        self.username = username
        self.password = password

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','username','password','created_on')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

db.create_all()
db.session.commit()