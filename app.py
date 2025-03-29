from flask import Flask
from config.config import SECRET_KEY
from routes.transaction import transaction_route
from routes.statistic import statistic_route

app = Flask(__file__)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(transaction_route)
app.register_blueprint(statistic_route)

if __name__ == "__main__":
    app.run("localhost", debug=True)