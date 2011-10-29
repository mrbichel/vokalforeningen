from django.contrib import admin
from files.models import File, Image

class FileAdmin(admin.ModelAdmin):
    list_display  = ('title', 'file', 'upload_date', 'mod_date')
    list_filter   = ('upload_date', 'mod_date')
    search_fields = ('title', 'file', 'description')

admin.site.register(File, FileAdmin)
admin.site.register(Image, FileAdmin)