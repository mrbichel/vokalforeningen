# -*- coding: utf-8 -*-

import datetime
from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User)
    url = models.URLField('Hjemmeside', blank=True)
    address = models.CharField('Adresse', max_length=255, blank=True)
    phone_number = models.CharField('Telefon', max_length=20, blank=True)
    member_since = models.DateField('Medlem siden', default=datetime.datetime.now)
    birthdate = models.DateField('Fødselsdato', blank=True)
    bio = models.TextField('Biografi', blank=True)

    #pub_date = models.DateTimeField(default=datetime.datetime.now)
    mod_date = models.DateTimeField(editable=False, default=datetime.datetime.now)

    image = ImageField(
        upload_to='images/profiles/',
        blank=True,
        null=True,
        help_text='Profilbillede.'
    )

    #lastfm = models.CharField(blank=True, )
    #googleplus = models.URLField(blank=True, )
    #uddannelse
    #stilling
    #facebook = models.CharField(blank=True, )
    #twitter models.CharField(blank=True, )

    def __unicode__(self):
        return self.user.username

    @models.permalink
    def get_absolute_url(self):
        return ('profile_detail', (),
            {'username': self.user.username,})


    class Meta:
        ordering = ['-mod_date']
        get_latest_by = 'mod_date'

    def save(self, *args, **kwargs):
        self.mod_date = datetime.datetime.now()
        super(Profile, self).save(*args, **kwargs)

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)