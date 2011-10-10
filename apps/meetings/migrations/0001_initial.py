# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Meeting'
        db.create_table('meetings_meeting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, db_index=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('mod_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('agenda', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('minutes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('meetings', ['Meeting'])


    def backwards(self, orm):
        
        # Deleting model 'Meeting'
        db.delete_table('meetings_meeting')


    models = {
        'meetings.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'agenda': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['meetings']
