from __future__ import unicode_literals
from django.db import models
import datetime
import os

from sorl.thumbnail import ImageField

def commonFileSave(self):
    self.mod_date = datetime.datetime.now()
    if not self.title:
        self.title = os.path.basename(self.file.name)

class CommonFileInfo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    upload_date = models.DateTimeField(default=datetime.datetime.now, editable=False)
    mod_date = models.DateTimeField(default=datetime.datetime.now, editable=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-upload_date']
        get_latest_by = 'upload_date'
        abstract = True

        verbose_name_plural = "filer"
        verbose_name = "fil"

    def get_absolute_url(self):
        return ''


class File(CommonFileInfo):
    file = models.FileField(
        upload_to="files/%Y/%m/",
    )

    def save(self, *args, **kwargs):
        commonFileSave(self)
        super(File, self).save(*args, **kwargs)

class Image(CommonFileInfo):
    file = ImageField(
        upload_to="images/%Y/%m/",
    )

    class Meta:
        verbose_name_plural = "billeder"
        verbose_name = "billede"

    def save(self, *args, **kwargs):
        commonFileSave(self)
        super(Image, self).save(*args, **kwargs)