# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models import signals

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("comment_posted", "Ny kommentar", "Der er kommet en ny kommentar på et indlæg du følger.")

    signals.post_syncdb.connect(create_notice_types, sender=notification)
else:
    print "Skipping creation of NoticeTypes as notification app not found"

