# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import Profile
from django.contrib.auth.models import User

admin.site.unregister(Profile)
admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = Profile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)


#
#admin.site.unregister(Profile)
#
#class ProfileAdmin(admin.ModelAdmin):
#    fieldsets = (
#        (None, {
#            'fields': ('url',
#                'address',
#                'postal_code',
#                'city',
#                'phone_number',
#                'mobile_phone_number',
#                'birthdate',
#                'bio',
#                'board_member',
#                'image',
#                'receive_email')
#        }),
#    )
#    list_display = ('postal_code', 'mod_date')
#    list_filter = ['board_member',]
#
#admin.site.register(Profile, ProfileAdmin)
#
