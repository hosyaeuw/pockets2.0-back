from flask import Blueprint
from flask_restful import Api, Resource

transactions = Blueprint('transactions', __name__)
api = Api(transactions)


class TransactionsApi(Resource):
    def get(self):
        return {
            'data': 'help',
        }


api.add_resource(TransactionsApi, '/transactions/')
