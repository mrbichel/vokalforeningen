# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from meetings.models import Meeting

class MeetingAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'agenda', 'minutes', 'pub_date')
        }),
    )
    list_display = ('title', 'date')
    list_filter = ['date']

admin.site.register(Meeting, MeetingAdmin)
