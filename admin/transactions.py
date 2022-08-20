from flask_admin.contrib.sqla import ModelView
from models import db, Transactions, TransactionCategories


class TransactionsModelsView(ModelView):
    pass


class TransactionCategoriesModelsView(ModelView):
    pass


transactions = TransactionsModelsView(
    Transactions,
    db.session,
    endpoint="/_transactions",
    category="Транзакции",
    name="Транзакции"
                                     )

transactions_categories = TransactionCategoriesModelsView(
    TransactionCategories,
    db.session,
    endpoint="/_transaction_categories",
    category="Транзакции",
    name="Категории"
                                                )
