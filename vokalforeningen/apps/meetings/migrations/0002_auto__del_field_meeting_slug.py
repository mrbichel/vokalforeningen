# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Meeting.slug'
        db.delete_column('meetings_meeting', 'slug')


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Meeting.slug'
        raise RuntimeError("Cannot reverse this migration. 'Meeting.slug' and its values cannot be restored.")


    models = {
        'meetings.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'agenda': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['meetings']
