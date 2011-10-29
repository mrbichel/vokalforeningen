# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Profile.postnr'
        db.add_column('profiles_profile', 'postnr', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5, null=True, blank=True), keep_default=False)

        # Adding field 'Profile.kommune'
        db.add_column('profiles_profile', 'kommune', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Profile.mobile_phone_numer'
        db.add_column('profiles_profile', 'mobile_phone_numer', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True), keep_default=False)

        # Adding field 'Profile.education'
        db.add_column('profiles_profile', 'education', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Profile.brancheerfaring'
        db.add_column('profiles_profile', 'brancheerfaring', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Profile.stilling'
        db.add_column('profiles_profile', 'stilling', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Profile.receive_email'
        db.add_column('profiles_profile', 'receive_email', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'Profile.member_since'
        db.alter_column('profiles_profile', 'member_since', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Profile.user'
        db.alter_column('profiles_profile', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))


    def backwards(self, orm):
        
        # Deleting field 'Profile.postnr'
        db.delete_column('profiles_profile', 'postnr')

        # Deleting field 'Profile.kommune'
        db.delete_column('profiles_profile', 'kommune')

        # Deleting field 'Profile.mobile_phone_numer'
        db.delete_column('profiles_profile', 'mobile_phone_numer')

        # Deleting field 'Profile.education'
        db.delete_column('profiles_profile', 'education')

        # Deleting field 'Profile.brancheerfaring'
        db.delete_column('profiles_profile', 'brancheerfaring')

        # Deleting field 'Profile.stilling'
        db.delete_column('profiles_profile', 'stilling')

        # Deleting field 'Profile.receive_email'
        db.delete_column('profiles_profile', 'receive_email')

        # Changing field 'Profile.member_since'
        db.alter_column('profiles_profile', 'member_since', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Profile.user'
        db.alter_column('profiles_profile', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True))


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
        'profiles.profile': {
            'Meta': {'ordering': "['-mod_date']", 'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'brancheerfaring': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'kommune': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'member_since': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'mobile_phone_numer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'postnr': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stilling': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['profiles']
