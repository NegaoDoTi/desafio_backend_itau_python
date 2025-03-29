from validators.date_validator import is_iso8601, is_past
from flask import Response

class TransactionController:
    
    def __init__(self):
        self.statistics:list = []
    
    def insert(self, req):
        try:
            data = req.get_json()
            
            if "valor" not in data or "dataHora" not in data:
                return 400
            
            if not isinstance(data["valor"], float) or data["valor"] < 0:
                return 422
            
            if not is_iso8601(data["dataHora"]) or not is_past("dataHora"):
                return 422
            
            self.statistics.append(data)
            
            return 201
        except:
            return 500
    
    def delete(self):
        try:
            self.statistics = []
            
            200
        
        except:
            return 500