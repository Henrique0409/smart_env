from flask import request, redirect, url_for, session, jsonify
from sqlalchemy import JSON
from app import app, db
from app.models import User
from flask_login import current_user, login_user, logout_user
import json



@app.route('/registrar', methods=['POST'])
def register():
    if request.method == 'POST':
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        json_data = User.to_json(nome, email, senha)
        if nome and email and senha:
            user = User(nome, email, senha)
            print(user)
            db.session.add(user)
            db.session.commit()
            print(json_data)
    return json.dumps(json_data)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.json['email']
        senha = request.json['senha']
        user =  User.query.filter_by(email=email).first()
        if not user and not user.verify_password(senha):
            print('Não  Logado')
        login_user(user)
        print(current_user.nome)    
    return f'Usuário logado {current_user.nome}'
    
@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return 'Usuário Deslogado'

app.run(host='0.0.0.0',debug=True)



