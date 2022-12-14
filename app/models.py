from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

#ao herdar o usermixin todos os metodos do flask login ja sao implementados em mixin.py
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

    def verify_password(self, pwd):
        return check_password_hash(self.senha, pwd)

    def to_json(nome, email, senha):
        return {'nome':nome,'email':email,'senha':generate_password_hash(senha)}

