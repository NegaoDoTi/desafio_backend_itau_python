from flask import Blueprint, request
from routes.transaction import transaction_controller
from controllers.StatisticController import StatisticController

statistic_route = Blueprint("statistic_route", __name__, url_prefix="/")

@statistic_route.route("/estatistica", methods=["GET"])
def get_statistics():
    if request.method == "GET":
        interval_seconds = request.args.get("intervaloSegundos", default=60, type=int)
        
        return StatisticController().get_statistics(transaction_controller.transactions, interval_seconds)