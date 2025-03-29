from validators.date_validator import is_iso8601
from flask import Response

class TransactionController:
    
    def __init__(self):
        self.statistics:list = []
    
    def insert(self, req):
        try:
            data = req.get_json()
            
            if "valor" not in data or "dataHora" not in data:
                return Response(status=400)
            
            if not isinstance(data["valor"], float):
                return Response(status=422)
            
            if not is_iso8601(data["dataHora"]):
                return Response(status=422)
            
            self.statistics.append(data)
            
            return Response(status=201)
        except:
            return Response(status=500)
    
    def delete(self):
        try:
            self.statistics = []
            
            Response(status=200)
        
        except:
            return Response(status=500)