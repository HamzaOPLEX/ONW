from tabnanny import verbose
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from ONW.ActionsManager.Ping import Ping
import logging

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore',verbose=False)
    register_events(scheduler)
    @scheduler.scheduled_job("cron",second='*/',name='auto_Ping')
    def auto_Ping():
        Ping()
    scheduler.start()
    # for job in scheduler.get_jobs():
    #     print("name: %s, trigger: %s, next run: %s, handler: %s" % (
    #       job.name, job.trigger, job.next_run_time, job.func))