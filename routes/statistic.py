from flask import Blueprint, request
from routes.transaction import transaction_controller
from controllers.StatisticController import StatisticController

statistic_route = Blueprint("statistic_route", __name__, url_prefix="/")

@statistic_route.route("/estatistica", methods=["GET"])
def get_statistics():
    if request.method == "GET":
        return StatisticController().get_statistics(transaction_controller.transactions)