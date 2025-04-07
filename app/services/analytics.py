import requests
from datetime import datetime

def log_click(short_code: str, ip_address: str):
    # Получаем данные о местоположении
    geo_data = requests.get(f"{os.getenv('IP_API_URL')}/{ip_address}").json()
    
    return {
        "short_code": short_code,
        "ip": ip_address,
        "country": geo_data.get("country"),
        "city": geo_data.get("city"),
        "timestamp": datetime.utcnow()
    }