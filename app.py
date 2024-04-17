from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models import db, ProductModel, UsuarioModel, PedidoModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db.init_app(app)

api = Api(app)

with app.app_context():

    db.create_all()


class Produto(Resource):
    def get(self, prod_id=None):

        if prod_id:
            prod = ProductModel.query.filter_by(id=prod_id).first()

            if prod:
                return {'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock}, 200
            else:
                return {'error': 'Task not found'}, 404

        else:

            prod = ProductModel.query.all()
            return [{'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock} for prod in

                    prod], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        parser.add_argument('price', type=float)
        parser.add_argument('stock', type=int)
        args = parser.parse_args()

        prod = ProductModel(name=args['name'], price=args['price'], stock=args['stock'])
        db.session.add(prod)
        db.session.commit()

        return {'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock}, 201

#######

class Cliente(Resource):
    def get(self, user_id=None):

        if user_id:
            user = UsuarioModel.query.filter_by(id=user_id).first()

            if user:
                return {'id': user.id, 'name': user.name, 'email': user.email, 'idade': user.idade}, 200
            else:
                return {'error': 'Task not found'}, 404

        else:

            user = UsuarioModel.query.all()
            return [{'id': user.id, 'name': user.name, 'email': user.email, 'idade': user.idade} for user  in

                    user], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        parser.add_argument('email', type=str)
        parser.add_argument('idade', type=int)
        args = parser.parse_args()

        user = UsuarioModel(name=args['name'], email=args['email'], idade=args['idade'])
        db.session.add(user)
        db.session.commit()

        return {'id': user.id, 'name': user.name, 'email': user.email, 'idade': user.idade}, 201

    

api.add_resource(Produto, '/products', '/products/<int:prod_id>')
api.add_resource(Cliente, '/user', '/user/<int:user_id>')



if __name__ == '__main__':

    app.run(debug=True)

