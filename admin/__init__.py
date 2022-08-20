from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


from app import app
from .transactions import transactions, transactions_categories


class AdminMixin:
    pass


class AdminView(AdminMixin, ModelView):
    pass


class HomeView(AdminMixin, AdminIndexView):
    pass


admin = Admin(app, 'Менеджер', url="/", index_view=HomeView(name="Главная"))
admin.add_view(transactions)
admin.add_view(transactions_categories)
