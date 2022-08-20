from flask import Blueprint, request
from flask_restful import Api, Resource
from models import Transactions, get_column_fields, get_attr, add_to_db, delete
from utils.DateHelper import DateHelper

transactions = Blueprint('transactions', __name__)
api = Api(transactions)


db_fields = get_column_fields(Transactions)


def generate_category_obj(category):
    if not category:
        return None

    return {
        'id': category.id,
        'name': category.name
    }


def generate_transaction_obj(transaction):
    return {
        'id': transaction.id,
        'category': generate_category_obj(transaction.category),
        'transaction_date': DateHelper.format_date(transaction.date),
        'amount': transaction.amount
    }


class TransactionsApi(Resource):
    def get(self):
        transactions = Transactions.query.all()
        return {
            'success': True,
            'result': [generate_transaction_obj(transaction)
                       for transaction in transactions]
        }

    def post(self):
        data = request.get_json(force=True)
        category = data.get('category')
        if category:
            data['transaction_category_id'] = category
        data['date'] = data['transaction_date']
        attr = get_attr(db_fields, data)

        t = Transactions(**attr)
        add_to_db([t])
        return {
            'success': True,
        }


class TransactionApi(Resource):
    def put(self, id):
        return {
            'success': True,
        }

    def delete(self, id):
        delete(Transactions, id)
        return {
            'success': True,
        }


api.add_resource(TransactionsApi, '/transactions/')
api.add_resource(TransactionApi, '/transactions/<id>/')
