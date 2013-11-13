# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HealthState'
        db.create_table(u'survey_healthstate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('actor_is_male', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_a_side_effect', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_transitional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('severity_rating', self.gf('django.db.models.fields.IntegerField')()),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('intro_body', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('vas_body', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('tto_body', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('outro_body', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'survey', ['HealthState'])

        # Adding model 'SurveyPath'
        db.create_table(u'survey_surveypath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
            ('state_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
            ('state_3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
            ('state_4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
            ('state_5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
            ('state_6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
            ('state_7', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
            ('state_8', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['survey.HealthState'])),
        ))
        db.send_create_signal(u'survey', ['SurveyPath'])

        # Adding model 'SurveyResponse'
        db.create_table(u'survey_surveyresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('entrance_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('exit_url', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'survey', ['SurveyResponse'])

        # Adding model 'HealthStateRating'
        db.create_table(u'survey_healthstaterating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey_response', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.SurveyResponse'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('vas_rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tto_rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('intro_started', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('intro_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('intro_completed_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('vas_started', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vas_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vas_completed_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tto_started', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tto_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tto_completed_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('outro_started', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('outro_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('outro_completed_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'survey', ['HealthStateRating'])


    def backwards(self, orm):
        # Deleting model 'HealthState'
        db.delete_table(u'survey_healthstate')

        # Deleting model 'SurveyPath'
        db.delete_table(u'survey_surveypath')

        # Deleting model 'SurveyResponse'
        db.delete_table(u'survey_surveyresponse')

        # Deleting model 'HealthStateRating'
        db.delete_table(u'survey_healthstaterating')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'survey.healthstate': {
            'Meta': {'object_name': 'HealthState'},
            'actor_is_male': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_a_side_effect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_transitional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'outro_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity_rating': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tto_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vas_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'survey.healthstaterating': {
            'Meta': {'object_name': 'HealthStateRating'},
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'intro_completed_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'intro_started': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'outro_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'outro_completed_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'outro_started': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'survey_response': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.SurveyResponse']"}),
            'tto_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tto_completed_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tto_rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tto_started': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vas_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vas_completed_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'vas_rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vas_started': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'survey.surveypath': {
            'Meta': {'object_name': 'SurveyPath'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"}),
            'state_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"}),
            'state_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"}),
            'state_4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"}),
            'state_5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"}),
            'state_6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"}),
            'state_7': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"}),
            'state_8': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['survey.HealthState']"})
        },
        u'survey.surveyresponse': {
            'Meta': {'object_name': 'SurveyResponse'},
            'entrance_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'exit_url': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['survey']