



# Chatbot para informações sobre o instituto de computação da UFBA
Repositório do projeto da equipe 1 do componente curricular MATE85 - Tópicos em Sistemas de Informação e Web I (UFBA).

Site para testes:

https://flask-chatb0t.herokuapp.com/

https://myflaskproject.pythonanywhere.com


### Documentação

* Diagrama de Arquitetura

https://github.com/pedroharzer/chatBotIC/raw/main/documentos/diagrama%20arquitetura.pdf

* Diagrama de Implantação

https://github.com/pedroharzer/chatBotIC/raw/main/documentos/Implanta%C3%A7%C3%A3o%20-%20IMG.pdf
<br>
https://github.com/pedroharzer/chatBotIC/raw/main/documentos/implanta%C3%A7%C3%A3o.pdf

* Postman:

https://documenter.getpostman.com/view/13068940/UUxxhoeE

* Planilha:

https://docs.google.com/spreadsheets/d/1LaCwHzLrI1kefqoY8yzLllXKLEX9HyDq_hXWkqZhySI/edit?usp=sharing

### Execução

#### Passos para executar o projeto:
1 - Clonar o repositório
```
git clone https://github.com/pedroharzer/chatBotIC.git
```
2 - Acessar o diretório
```
cd chatBotIC
```
3 - Instalar as dependências
```
pip install -r requirements.txt
```
4 - Executar o projeto
```
cd backend
export FLASK_APP=app.py
flask run
```

## EQUIPE:

**Backend**<br>
Felipe Rebouças Ferreira Abreu<br>
Pedro Henrique Harzer Santana<br>

**Frontend**<br>
Milo Raziel Santos Rodrigues<br>

**Atividades**<br>

Felipe - Arquitetura do Backend, Frontend provisório<br>
Pedro - Funções auxiliares, documentação do projeto<br>
Milo - Frontend definitivo<br>

## TECNOLOGIAS UTILIZADAS

### Desenvolvimento

**Front-end** <br>
BoostStrap

**Back-end:** <br>
Python utilizando o framework Flask

**Banco de dados:**<br>
MongoDB
<br>
**Controle de versão:**<br>
GitHub

### Deploy

**Front-end**<br>
Vercel

**Back-end**<br>
Heroku


**Planejamento**<br>

Integração da API com o banco de dados - Concluído ✔️
<br>
Diagrama de implantação - Concluído ✔️ (Pedro)
<br>
Diagrama de arquitetura - Concluído ✔️ (Felipe)
<br>
Tratamento de entradas em Regex - Concluído ✔️
<br>
Sistema de sugestões - Concluído ✔️
<br>
Cadastro de perguntas e respostas via API - Concluído ✔️
<br>
Documentação da API - Concluído ✔️ (Pedro e Felipe)
<br>
CRUD - Parcial (falta a interface) ➖ 
<br>
Implementação do novo framework de frontend - Não realizado (em andamento) ❌
<br>
Deploy em servidor Heroku - Concluído ✔️
<br>
Proteger as rotas em JWT - Parcial (implementado para acesso ao cadastro de perguntas, mas pendente para o resto do CRUD) ➖ 
<br>
Sistema de cadastro e login - Concluído ✔️ (Felipe)



*OBS: No decorrer do projeto, a equipe poderá alterar um ou mais aspectos ou tecnologias que serão utilizadas.*
