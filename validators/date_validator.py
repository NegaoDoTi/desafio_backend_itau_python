from re import match
from dateutil.parser import isoparse
from datetime import datetime

def is_iso8601(data_string:str) -> bool:
    iso8601_re = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}[+-]\d{2}:\d{2}$"
    
    if not isinstance(data_string, str):
        return False
        
    if bool(match(iso8601_re, data_string)):
        try:
            isoparse(data_string)
            return True
        
        except ValueError:
            return False
        
    return False

def is_past(data_string:str) -> bool:
    
    date_req = isoparse(data_string)
    
    now = datetime.now(date_req.tzinfo)
    
    return date_req <= now

def last_seconds(date_string:str, interval_seconds:int = 60) -> bool:
    date_req = isoparse(date_string)
    
    now = datetime.now(date_req.tzinfo)
    
    verify = (now - date_req).total_seconds()
    
    return 0 <= verify <= interval_seconds