# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HealthState.number'
        db.add_column(u'survey_healthstate', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'SurveyPath.used'
        db.add_column(u'survey_surveypath', 'used',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Renaming column for 'SurveyPath.state_8' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_8_id', 'state_8')
        # Changing field 'SurveyPath.state_8'
        db.alter_column(u'survey_surveypath', 'state_8', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_8']
        db.delete_index(u'survey_surveypath', ['state_8_id'])


        # Renaming column for 'SurveyPath.state_1' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_1_id', 'state_1')
        # Changing field 'SurveyPath.state_1'
        db.alter_column(u'survey_surveypath', 'state_1', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_1']
        db.delete_index(u'survey_surveypath', ['state_1_id'])


        # Renaming column for 'SurveyPath.state_3' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_3_id', 'state_3')
        # Changing field 'SurveyPath.state_3'
        db.alter_column(u'survey_surveypath', 'state_3', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_3']
        db.delete_index(u'survey_surveypath', ['state_3_id'])


        # Renaming column for 'SurveyPath.state_2' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_2_id', 'state_2')
        # Changing field 'SurveyPath.state_2'
        db.alter_column(u'survey_surveypath', 'state_2', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_2']
        db.delete_index(u'survey_surveypath', ['state_2_id'])


        # Renaming column for 'SurveyPath.state_5' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_5_id', 'state_5')
        # Changing field 'SurveyPath.state_5'
        db.alter_column(u'survey_surveypath', 'state_5', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_5']
        db.delete_index(u'survey_surveypath', ['state_5_id'])


        # Renaming column for 'SurveyPath.state_4' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_4_id', 'state_4')
        # Changing field 'SurveyPath.state_4'
        db.alter_column(u'survey_surveypath', 'state_4', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_4']
        db.delete_index(u'survey_surveypath', ['state_4_id'])


        # Renaming column for 'SurveyPath.state_7' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_7_id', 'state_7')
        # Changing field 'SurveyPath.state_7'
        db.alter_column(u'survey_surveypath', 'state_7', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_7']
        db.delete_index(u'survey_surveypath', ['state_7_id'])


        # Renaming column for 'SurveyPath.state_6' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_6_id', 'state_6')
        # Changing field 'SurveyPath.state_6'
        db.alter_column(u'survey_surveypath', 'state_6', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'SurveyPath', fields ['state_6']
        db.delete_index(u'survey_surveypath', ['state_6_id'])


    def backwards(self, orm):
        # Adding index on 'SurveyPath', fields ['state_6']
        db.create_index(u'survey_surveypath', ['state_6_id'])

        # Adding index on 'SurveyPath', fields ['state_7']
        db.create_index(u'survey_surveypath', ['state_7_id'])

        # Adding index on 'SurveyPath', fields ['state_4']
        db.create_index(u'survey_surveypath', ['state_4_id'])

        # Adding index on 'SurveyPath', fields ['state_5']
        db.create_index(u'survey_surveypath', ['state_5_id'])

        # Adding index on 'SurveyPath', fields ['state_2']
        db.create_index(u'survey_surveypath', ['state_2_id'])

        # Adding index on 'SurveyPath', fields ['state_3']
        db.create_index(u'survey_surveypath', ['state_3_id'])

        # Adding index on 'SurveyPath', fields ['state_1']
        db.create_index(u'survey_surveypath', ['state_1_id'])

        # Adding index on 'SurveyPath', fields ['state_8']
        db.create_index(u'survey_surveypath', ['state_8_id'])

        # Deleting field 'HealthState.number'
        db.delete_column(u'survey_healthstate', 'number')

        # Deleting field 'SurveyPath.used'
        db.delete_column(u'survey_surveypath', 'used')


        # Renaming column for 'SurveyPath.state_8' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_8', 'state_8_id')
        # Changing field 'SurveyPath.state_8'
        db.alter_column(u'survey_surveypath', 'state_8_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

        # Renaming column for 'SurveyPath.state_1' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_1', 'state_1_id')
        # Changing field 'SurveyPath.state_1'
        db.alter_column(u'survey_surveypath', 'state_1_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

        # Renaming column for 'SurveyPath.state_3' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_3', 'state_3_id')
        # Changing field 'SurveyPath.state_3'
        db.alter_column(u'survey_surveypath', 'state_3_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

        # Renaming column for 'SurveyPath.state_2' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_2', 'state_2_id')
        # Changing field 'SurveyPath.state_2'
        db.alter_column(u'survey_surveypath', 'state_2_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

        # Renaming column for 'SurveyPath.state_5' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_5', 'state_5_id')
        # Changing field 'SurveyPath.state_5'
        db.alter_column(u'survey_surveypath', 'state_5_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

        # Renaming column for 'SurveyPath.state_4' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_4', 'state_4_id')
        # Changing field 'SurveyPath.state_4'
        db.alter_column(u'survey_surveypath', 'state_4_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

        # Renaming column for 'SurveyPath.state_7' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_7', 'state_7_id')
        # Changing field 'SurveyPath.state_7'
        db.alter_column(u'survey_surveypath', 'state_7_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

        # Renaming column for 'SurveyPath.state_6' to match new field type.
        db.rename_column(u'survey_surveypath', 'state_6', 'state_6_id')
        # Changing field 'SurveyPath.state_6'
        db.alter_column(u'survey_surveypath', 'state_6_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.HealthState']))

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
            'number': ('django.db.models.fields.IntegerField', [], {}),
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
            'health_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.HealthState']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'intro_completed_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'intro_started': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
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
        u'survey.healthstatesequenceupload': {
            'Meta': {'object_name': 'HealthStateSequenceUpload'},
            'csv_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'survey.surveypath': {
            'Meta': {'object_name': 'SurveyPath'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'state_1': ('django.db.models.fields.IntegerField', [], {}),
            'state_2': ('django.db.models.fields.IntegerField', [], {}),
            'state_3': ('django.db.models.fields.IntegerField', [], {}),
            'state_4': ('django.db.models.fields.IntegerField', [], {}),
            'state_5': ('django.db.models.fields.IntegerField', [], {}),
            'state_6': ('django.db.models.fields.IntegerField', [], {}),
            'state_7': ('django.db.models.fields.IntegerField', [], {}),
            'state_8': ('django.db.models.fields.IntegerField', [], {}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'survey.surveyresponse': {
            'Meta': {'object_name': 'SurveyResponse'},
            'entrance_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'exit_url': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'state_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'state_3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'state_4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'state_5': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'state_6': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'state_7': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'state_8': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['survey.HealthState']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['survey']