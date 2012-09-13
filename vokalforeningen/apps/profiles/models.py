# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField
from django.db.models.signals import post_save, post_delete
import mailchimp

class Profile(models.Model):
    user = models.OneToOneField(User)
    url = models.URLField('Hjemmeside', blank=True)
    address = models.CharField('Adresse', max_length=255, blank=True)
    postal_code = models.PositiveIntegerField(max_length=5, blank=True, null=True)
    city = models.CharField('By', max_length=255, blank=True)
    phone_number = models.CharField('Telefon', max_length=20, blank=True)
    mobile_phone_number = models.CharField('Mobil telefon', max_length=20, blank=True)
    birthdate = models.DateField('Fødselsdato', blank=True, null=True)
    bio = models.TextField('Biografi', blank=True)
    
    mod_date = models.DateTimeField(editable=False, default=datetime.datetime.now)

    image = ImageField('Profilbillede',
        upload_to='images/profiles/',
        blank=True,
        null=True,
        help_text='Profilbillede.'
    )

    #lastfm = models.CharField(blank=True, )
    #googleplus = models.URLField(blank=True, )

    facebook = models.URLField(blank=True, )

    education = models.TextField('Uddannelse', blank=True)
    experience = models.TextField('Brancheerfaring', blank=True)
    position = models.TextField('Stilling', blank=True)

    receive_email = models.BooleanField('Modtag email',
            help_text="Kryds af hvis du vil modtage emails når der er nye kommentarer på indlæg du selv har skrevet eller kommenteret på.")

    def __unicode__(self):
        return self.user.username

    @models.permalink
    def get_absolute_url(self):
        return ('profile_detail', (),
            {'id': self.user.id,})

    class Meta:
        ordering = ['-mod_date']
        get_latest_by = 'mod_date'

    def save(self, *args, **kwargs):
        self.mod_date = datetime.datetime.now()
        super(Profile, self).save(*args, **kwargs)


def user_updated(sender, instance, created, **kwargs):
    if sender is User and created:
        Profile.objects.create(user=instance)
    else:
        if sender is Profile:
            user = instance.user
        else:
            user = instance

        mailchimp.updateProfile(user)  
        
post_save.connect(user_updated, sender=User)
post_save.connect(user_updated, sender=Profile)

def user_deleted(sender, instance, **kwargs):
    mailchimp.unsubscribe(instance)

post_delete.connect(user_deleted, sender=User)