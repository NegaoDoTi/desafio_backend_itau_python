from validators.date_validator import last_seconds
from flask import jsonify


class StatisticController:

    def get_statistics(self, transactions:list):
        try:
            valid_values = []
            
            for transaction in transactions:
                
                key = next(iter(transaction))
                
                if last_seconds(key):
                    valid_values.append(transaction[key]["valor"])
            
            len_valid_values = len(valid_values)
            
            if len_valid_values == 0:
                return jsonify(
                    {
                        "count" : 0,
                        "sum" : 0,
                        "avg" : 0,
                        "min" : 0,
                        "max" : 0
                    }
                ), 200
            
            sum_valid_values = sum(valid_values)
            
            return jsonify(
                {
                    "count" : len_valid_values,
                    "sum" : round(sum_valid_values, 2),
                    "avg" : round(sum_valid_values/len_valid_values, 2),
                    "min" : round(min(valid_values),2),
                    "max" : round(max(valid_values), 2)
                }
            ), 200
        
        except:
            return "", 500