# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Event'
        db.delete_table('corkboard_event')

        # Adding field 'Note.is_event'
        db.add_column('corkboard_note', 'is_event', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Note.start'
        db.add_column('corkboard_note', 'start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Note.end'
        db.add_column('corkboard_note', 'end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Note.location'
        db.add_column('corkboard_note', 'location', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Note.facebook'
        db.add_column('corkboard_note', 'facebook', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Event'
        db.create_table('corkboard_event', (
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('note_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['corkboard.Note'], unique=True, primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('corkboard', ['Event'])

        # Deleting field 'Note.is_event'
        db.delete_column('corkboard_note', 'is_event')

        # Deleting field 'Note.start'
        db.delete_column('corkboard_note', 'start')

        # Deleting field 'Note.end'
        db.delete_column('corkboard_note', 'end')

        # Deleting field 'Note.location'
        db.delete_column('corkboard_note', 'location')

        # Deleting field 'Note.facebook'
        db.delete_column('corkboard_note', 'facebook')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'corkboard.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'corkboard.note': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Note'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corkboard.Category']", 'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_event': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['corkboard']
