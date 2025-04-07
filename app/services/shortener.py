from hashids import Hashids
from datetime import datetime, timedelta
import os

hashids = Hashids(min_length=4, salt=os.getenv("HASHIDS_SALT", "default_salt"))

def generate_short_code(url_id: int) -> str:
    return hashids.encode(url_id)

def calculate_expiry(days: int = 7) -> datetime:
    return datetime.utcnow() + timedelta(days=days)