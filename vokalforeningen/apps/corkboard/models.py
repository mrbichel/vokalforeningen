# -*- coding: utf-8 -*-

import datetime
import pprint
from django_comments.signals import comment_was_posted
from django.db.models.signals import post_save
from django_comments.models import Comment

from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_app
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User
from markdown2 import markdown

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "kategorier"
        verbose_name = "kategori"

class Note(models.Model):
    title = models.CharField(u"Titel", max_length=60)
    author = models.ForeignKey(User)
    body = models.TextField(u"Brødtekst")
    html = models.TextField(editable=False)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    mod_date = models.DateTimeField(editable=False, default=datetime.datetime.now)
    category = models.ForeignKey(Category, blank=True, null=True)

    is_event = models.BooleanField(default=False, editable=False)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField("Slut", blank=True, null=True)
    location = models.CharField("Sted", max_length=255, blank=True)
    facebook = models.URLField("Facebook link", blank=True)

    class Meta:
        get_latest_by = 'pub_date'
        verbose_name_plural = "noter"
        verbose_name = "note"


    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'note_detail', (), {'id': self.id,}

    def save(self, *args, **kwargs):
        self.mod_date = datetime.datetime.now()
        self.html = unicode(markdown(self.body))
        super(Note, self).save(*args, **kwargs)

try:
    notification = get_app( 'notification' )
except ImproperlyConfigured:
    notification = None



def send_comment_notification(sender, comment, request, **kwargs):
    # no point in proceeding if notification is not available
    if not notification:
        return

    # get comment's content object and its ctype
    obj = comment.content_object

    data = {
        'comment': comment,
        'object': obj,
    }

    comments = Comment.objects.filter(
            content_type=comment.content_type,
            object_pk=obj.id
        ).exclude(user=comment.user)

    users = []
    def appendUser(u):
        if u not in users and u.profile.receive_email and u.is_active:
            users.append(u)

    if comment.user.id is not obj.author.id:
        appendUser(obj.author)
    for c in comments:
        appendUser(c.user)

    pprint.pprint(users)

    notification.send(users, 'comment_posted', data)


# connect signal
comment_was_posted.connect(send_comment_notification)


@receiver(post_save, sender=Note)
def send_post_notification(sender, **kwargs):
    # no point in proceeding if notification is not available
    if not notification:
        return

    note = kwargs['instance']

    data = {
        'note': note,
    }

    users = User.objects.filter(is_active=True, profile__receive_email=True).exclude(id=note.author.id)
    notification.send(users, 'note_posted', data)
