from app import db
from datetime import datetime


def get_attr(db_fields, args):
    return {db_field: args[db_field] for db_field in db_fields if args.get(db_field)}


def get_column_fields(obj):
    return obj.metadata.tables[obj.__tablename__].columns.keys()

def add_to_db(obj):
    try:
        if not isinstance(obj, list):
            obj = [obj]
        db.session.add_all(obj)
        db.session.commit()
    # TODO: оплавливать определенные ошибки
    except Exception as e:
        raise e

def delete(table, id):
    try:
        table.query.filter(table.id == id).delete()
        db.session.commit()
    # TODO: оплавливать определенные ошибки
    except Exception as e:
        raise e


class TransactionCategories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    transaction = db.relationship('Transactions',
                                  backref=db.backref('category', lazy=True))

    def __init__(self, **kwargs):
        super(TransactionCategories, self).__init__(**kwargs)

    def __repr__(self):
        return self.name


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, default=datetime.now()) # rename to transaction_date

    transaction_category_id = db.Column(db.Integer,
                                        db.ForeignKey(
                                            'transaction_categories.id',
                                            ondelete="NO ACTION"),
                                        nullable=True)

    def __init__(self, **kwargs):
        super(Transactions, self).__init__(**kwargs)

    def __repr__(self):
        return f'{self.amount, self.date}'


if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
    # db.session.commit()
