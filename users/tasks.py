from celery import shared_task
from django.core.mail import EmailMessage
from datetime import date, timedelta
import logging

logger = logging.getLogger(__name__)


@shared_task
def collect_data():
    pass
