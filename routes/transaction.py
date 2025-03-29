from flask import Blueprint, request

transaction_route = Blueprint("transaction_route", __name__, url_prefix="/")

@transaction_route.route("/transacao", methods=["POST"])
def insert_transaction():
    if request.method == "GET":
        pass
    else:
        return 405
