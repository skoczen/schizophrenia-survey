# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SurveyResponse.age'
        db.add_column(u'survey_surveyresponse', 'age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SurveyResponse.education'
        db.add_column(u'survey_surveyresponse', 'education',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SurveyResponse.household_income'
        db.add_column(u'survey_surveyresponse', 'household_income',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SurveyResponse.diagnosed_with_serious_mental_illness'
        db.add_column(u'survey_surveyresponse', 'diagnosed_with_serious_mental_illness',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.diagnosed_with_schizophrenia'
        db.add_column(u'survey_surveyresponse', 'diagnosed_with_schizophrenia',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.diagnosed_with_depression'
        db.add_column(u'survey_surveyresponse', 'diagnosed_with_depression',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.diagnosed_with_bipolar'
        db.add_column(u'survey_surveyresponse', 'diagnosed_with_bipolar',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.diagnosed_with_other'
        db.add_column(u'survey_surveyresponse', 'diagnosed_with_other',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.diagnosed_with_dont_know'
        db.add_column(u'survey_surveyresponse', 'diagnosed_with_dont_know',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.family_diagnosed_with_serious_mental_illness'
        db.add_column(u'survey_surveyresponse', 'family_diagnosed_with_serious_mental_illness',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.family_diagnosed_with_schizophrenia'
        db.add_column(u'survey_surveyresponse', 'family_diagnosed_with_schizophrenia',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.family_diagnosed_with_depression'
        db.add_column(u'survey_surveyresponse', 'family_diagnosed_with_depression',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.family_diagnosed_with_bipolar'
        db.add_column(u'survey_surveyresponse', 'family_diagnosed_with_bipolar',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.family_diagnosed_with_other'
        db.add_column(u'survey_surveyresponse', 'family_diagnosed_with_other',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SurveyResponse.family_diagnosed_with_dont_know'
        db.add_column(u'survey_surveyresponse', 'family_diagnosed_with_dont_know',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SurveyResponse.age'
        db.delete_column(u'survey_surveyresponse', 'age')

        # Deleting field 'SurveyResponse.education'
        db.delete_column(u'survey_surveyresponse', 'education')

        # Deleting field 'SurveyResponse.household_income'
        db.delete_column(u'survey_surveyresponse', 'household_income')

        # Deleting field 'SurveyResponse.diagnosed_with_serious_mental_illness'
        db.delete_column(u'survey_surveyresponse', 'diagnosed_with_serious_mental_illness')

        # Deleting field 'SurveyResponse.diagnosed_with_schizophrenia'
        db.delete_column(u'survey_surveyresponse', 'diagnosed_with_schizophrenia')

        # Deleting field 'SurveyResponse.diagnosed_with_depression'
        db.delete_column(u'survey_surveyresponse', 'diagnosed_with_depression')

        # Deleting field 'SurveyResponse.diagnosed_with_bipolar'
        db.delete_column(u'survey_surveyresponse', 'diagnosed_with_bipolar')

        # Deleting field 'SurveyResponse.diagnosed_with_other'
        db.delete_column(u'survey_surveyresponse', 'diagnosed_with_other')

        # Deleting field 'SurveyResponse.diagnosed_with_dont_know'
        db.delete_column(u'survey_surveyresponse', 'diagnosed_with_dont_know')

        # Deleting field 'SurveyResponse.family_diagnosed_with_serious_mental_illness'
        db.delete_column(u'survey_surveyresponse', 'family_diagnosed_with_serious_mental_illness')

        # Deleting field 'SurveyResponse.family_diagnosed_with_schizophrenia'
        db.delete_column(u'survey_surveyresponse', 'family_diagnosed_with_schizophrenia')

        # Deleting field 'SurveyResponse.family_diagnosed_with_depression'
        db.delete_column(u'survey_surveyresponse', 'family_diagnosed_with_depression')

        # Deleting field 'SurveyResponse.family_diagnosed_with_bipolar'
        db.delete_column(u'survey_surveyresponse', 'family_diagnosed_with_bipolar')

        # Deleting field 'SurveyResponse.family_diagnosed_with_other'
        db.delete_column(u'survey_surveyresponse', 'family_diagnosed_with_other')

        # Deleting field 'SurveyResponse.family_diagnosed_with_dont_know'
        db.delete_column(u'survey_surveyresponse', 'family_diagnosed_with_dont_know')


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
        u'survey.actionlog': {
            'Meta': {'object_name': 'ActionLog'},
            'action': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'when': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'survey.healthstate': {
            'Meta': {'object_name': 'HealthState'},
            'actor_is_male': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_a_side_effect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_transitional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
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
        u'survey.surveyaggregatestats': {
            'Meta': {'object_name': 'SurveyAggregateStats'},
            'average_survey_progress': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'completion_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dwell_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'survey.surveyexport': {
            'Meta': {'object_name': 'SurveyExport'},
            'csv_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'export_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_rows': ('django.db.models.fields.IntegerField', [], {})
        },
        u'survey.surveypath': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SurveyPath'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
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
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosed_with_bipolar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosed_with_depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosed_with_dont_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosed_with_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosed_with_schizophrenia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosed_with_serious_mental_illness': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'entrance_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'exit_url': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'family_diagnosed_with_bipolar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_diagnosed_with_depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_diagnosed_with_dont_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_diagnosed_with_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_diagnosed_with_schizophrenia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_diagnosed_with_serious_mental_illness': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'household_income': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'state_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'state_3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'state_4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'state_5': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'state_6': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'state_7': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'state_8': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['survey.HealthState']"}),
            'survey_path_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['survey']