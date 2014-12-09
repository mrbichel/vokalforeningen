# -*- coding: utf-8 -*-

from django.contrib import admin
from corkboard.models import Note, Category

class NoteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'body', 'pub_date', 'category')
        }),
    )
    list_display = ('title', 'author', 'pub_date', 'mod_date')
    list_filter = ['pub_date', 'mod_date', 'category']

admin.site.register(Note, NoteAdmin)

admin.site.register(Category, admin.ModelAdmin)
