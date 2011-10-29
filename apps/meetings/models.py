import datetime
from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=150)

    date = models.DateTimeField()

    pub_date = models.DateTimeField(default=datetime.datetime.now)
    mod_date = models.DateTimeField(editable=False, default=datetime.datetime.now)

    agenda = models.TextField(blank=True)
    minutes = models.TextField(blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('meeting_detail', (), {'id': self.id,})