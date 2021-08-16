#Este é um código que deve ser executando usando o pytest. Ele realiza testes automatizados na API em execução.

import requests
import pytest
import time
from requests.auth import HTTPBasicAuth
import json

token=""
bearerstring = ""

#Cadastrar usuário

def teste1():

    response = requests.post('http://127.0.0.1:5000/user', json={'username': 'felipe', 'password': '123'})
    assert response.status_code == 201

#Tentar cadastrar usuário com o mesmo nome

def teste2():

    response = requests.post('http://127.0.0.1:5000/user', json={'username': 'felipe', 'password': '456'})
    assert response.status_code == 500
    
#Realizar login com dado errado
    
def teste3():
    response = requests.post('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('felipe', '1234'))

    assert response.status_code == 401

#Realizar login com dado correto
    
def teste4():
    response = requests.post('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('felipe', '123'))
    global token
    token = response.json()['token']
    assert response.status_code == 200

#Alterar dados cadastrais

def teste5():
    global bearerstring
    global token
    bearerstring = "Bearer "+token
    headers = {"Authorization": bearerstring}
    response = requests.put('http://127.0.0.1:5000/user', json={'username': 'felipea', 'password': '1234'},headers=headers)
    assert response.status_code == 201

#Logar novamente com as novas credenciais

def teste6():
    response = requests.post('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('felipea', '1234'))
    global token
    token = response.json()['token']
    assert response.status_code == 200

#Acessar home

def teste7():
    global bearerstring
    global token
    bearerstring = "Bearer "+token
    headers = {"Authorization": bearerstring}
    response = requests.get('http://127.0.0.1:5000/home',headers=headers)
    assert response.status_code == 200


#Realizar aposta

def teste8():
    global bearerstring
    headers = {"Authorization": bearerstring}
    response = requests.post('http://127.0.0.1:5000/lotrealizarjogo',json={'ndezenas':6},headers=headers)
    assert response.status_code == 201

#Realizar aposta com dezenas definidas

def teste9():
    global bearerstring
    headers = {"Authorization": bearerstring}
    response = requests.post('http://127.0.0.1:5000/lotrealizarjogo',json={'ndezenas':6, 'dezenas':[1,2,3,4,5,6]},headers=headers)
    assert response.status_code == 201

#Retornar resultado da Mega Sena

def teste10():
    global bearerstring
    headers = {"Authorization": bearerstring}
    response = requests.get('http://127.0.0.1:5000/consultarresultado',headers=headers)
    assert response.status_code == 200

#Verificar jogos passados

def teste11():
    global bearerstring
    headers = {"Authorization": bearerstring}
    response = requests.get('http://127.0.0.1:5000/jogospassados',headers=headers)
    assert response.status_code == 200

#Apagar o cadastro

def teste12():
    global bearerstring
    headers = {"Authorization": bearerstring}
    response = requests.delete('http://127.0.0.1:5000/user',headers=headers)
    assert response.status_code == 200
    
