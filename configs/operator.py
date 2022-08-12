from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from ONW.ActionsManager.Ping import Ping


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)

    @scheduler.scheduled_job("cron", day_of_week='mon-fri', hour=20, minute=38,name='auto_Ping')
    def auto_Ping():
        Ping()

    scheduler.start()