from django.db import models

class groups(models.Model):
    # app_id = models.CharField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ':' + self.app_id

class hosts(models.Model):
    # app_id = models.CharField(max_length=50, blank=False, null=False)
    hostname = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    group = models.ForeignKey(groups,on_delete=models.RESTRICT)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        print(self.id)
        return self.hostname + ':' + self.app_id

class network_events(models.Model):
    # app_id = models.CharField(max_length=50, blank=False, null=False)
    event_host = models.ForeignKey(hosts,on_delete=models.RESTRICT)
    event_status = models.IntegerField(default=0)
    event_time = models.DateTimeField(auto_now_add=True)
    event_desc = models.CharField(max_length=50)

    def __str__(self):
        return self.event_desc

class backend_settings(models.Model):
    notification_email = models.EmailField(max_length=50)
    app_admin_email = models.EmailField(max_length=50)
    smtp_server = models.CharField(max_length=50)
    def __str__(self):
        return {
            'notification_email': self.notification_email,
            'app_admin_email': self.app_admin_email,
            'smtp_server': self.smtp_server,
        }