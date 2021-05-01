from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .api import update


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', seconds=5)
    scheduler.start()