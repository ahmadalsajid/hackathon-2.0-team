from celery import shared_task
from django.core.mail import EmailMessage
from datetime import date, timedelta
from users.models import Video, Tiktoker
import logging

logger = logging.getLogger(__name__)


@shared_task
def collect_data():
    print('task running')
    # videos = [ {
    #     'url':'',
    # }]
    # for video in videos:
    #     _v = Video.objects.create(**video)
    #
    # tiktokers = []
    # for t in tiktokers:
    #     _t = Tiktoker.objects.create(**t)
