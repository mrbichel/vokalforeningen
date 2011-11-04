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
    postal_code = models.PositiveIntegerField(max_length=5, blank=True, null=True)
    city = models.CharField('By', max_length=255, blank=True)
    phone_number = models.CharField('Telefon', max_length=20, blank=True)
    mobile_phone_number = models.CharField('Mobil telefon', max_length=20, blank=True)
    birthdate = models.DateField('Fødselsdato', blank=True)
    bio = models.TextField('Biografi', blank=True)
    board_member = models.BooleanField(default=False)

    mod_date = models.DateTimeField(editable=False, default=datetime.datetime.now)

    image = ImageField(
        upload_to='images/profiles/',
        blank=True,
        null=True,
        help_text='Profilbillede.'
    )

    #lastfm = models.CharField(blank=True, )
    #googleplus = models.URLField(blank=True, )
    education = models.TextField('Uddannelse', blank=True)
    experience = models.TextField('Brancheerfaring', blank=True)
    position = models.TextField('Stilling', blank=True)

    receive_email = models.BooleanField()

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

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)