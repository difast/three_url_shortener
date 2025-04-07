from celery import Celery
from app.services.analytics import log_click
import os

celery = Celery(__name__)
celery.conf.broker_url = os.getenv("CELERY_BROKER_URL")
celery.conf.result_backend = os.getenv("CELERY_RESULT_BACKEND")

@celery.task
def process_click_analytics(short_code: str, ip_address: str):
    return log_click(short_code, ip_address)