from validators.date_validator import is_iso8601, is_past
from datetime import datetime

class TransactionController:
    
    def __init__(self):
        self.transactions:list = []
    
    def insert(self, req):
        try:
            data = req.get_json()
            
            if "valor" not in data or "dataHora" not in data:
                return "", 400
            
            if not isinstance(data["valor"], float) or data["valor"] < 0:
                return "", 422
            
            if not is_iso8601(data["dataHora"]) or not is_past(data["dataHora"]):
                return "", 422
            
            now = datetime.now().isoformat()
            
            transaction = {
                f"{now}" : data
            }
            
            self.transactions.append(transaction)
            
            return "", 201
        except:
            return "", 500
    
    def delete(self):
        try:
            self.transactions = []
            
            return "", 200
        
        except:
            return "", 500