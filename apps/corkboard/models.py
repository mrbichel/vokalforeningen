import datetime
from django.db import models
from django.contrib.auth.models import User
from markdown2 import markdown

class Category(models.Model):
    name = models.CharField(max_length=40)

class Note(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(User)
    body = models.TextField()
    html = models.TextField(editable=False, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    mod_date = models.DateTimeField(editable=False, default=datetime.datetime.now)
    category = models.ForeignKey(Category, blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('note_detail', (), {'id': self.id,})

    def save(self, *args, **kwargs):
        self.mod_date = datetime.datetime.now()
        self.html = markdown(self.body)
        super(Note, self).save(*args, **kwargs)

