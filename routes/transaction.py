from flask import Blueprint, request, Response
from controllers.TransactionController import TransactionController

transaction_route = Blueprint("transaction_route", __name__, url_prefix="/")

transaction_controller = TransactionController()

@transaction_route.route("/transacao", methods=["POST"])
def insert_transaction():
    if request.method == "POST":
        print(transaction_controller.transactions)
        return transaction_controller.insert(request)

@transaction_route.route("/transacao", methods=["DELETE"])
def delete_all_transaction():
    if request.method == "DELETE":
        print(transaction_controller.transactions)
        return transaction_controller.delete()