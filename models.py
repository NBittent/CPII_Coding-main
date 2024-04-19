from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ProductModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    price = db.Column(db.Float, nullable=False)

    stock= db.Column(db.Integer, nullable=False)

class PedidoModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    usuario_id = db.Column(db.Integer, nullable=False)

    descricao = db.Column(db.String(100), nullable=False)

    status = db.Column(db.String(20), nullable=False)

    id_produto = db.Column(db.Integer, nullable=False)

class UsuarioModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(30), nullable=False)

    idade = db.Column(db.Integer, nullable=False)


def __repr__(self):


    return f'<Product {self.name}>'