from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=150)

    date = models.DateTimeField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()

    agenda = models.TextField(blank=True)
    minutes = models.TextField(blank=True)

