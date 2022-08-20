from app import app

from transactions import transactions

app.register_blueprint(transactions, url_prefix="/api")

if __name__ == '__main__':
    app.run()
