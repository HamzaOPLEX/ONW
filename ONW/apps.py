from django.apps import AppConfig
from django.conf import settings


class ONWappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ONW'
    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from configs import operator 
            operator.start()
            