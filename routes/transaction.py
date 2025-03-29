from flask import Blueprint, request, Response
from controllers.TransactionController import TransactionController

transaction_route = Blueprint("transaction_route", __name__, url_prefix="/")

transactions = TransactionController()

@transaction_route.route("/transacao", methods=["POST"])
def insert_transaction():
    if request.method == "POST":
        print(transactions.statistics)
        transactions.insert(request)

@transaction_route.route("/transacao", methods=["DELETE"])
def delete_all_transaction():
    if request.method == "DELETE":
        print(transactions.statistics)
        transactions.delete()