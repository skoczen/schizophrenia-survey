# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        super_admin_group = orm['auth.group'].objects.get_or_create(name="Survey Super-Admins")[0]

        # Survey Super-admins.
        # Should be VERY limited.

        # HealthState
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='add_healthstate'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='change_healthstate'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='delete_healthstate'))

        # SurveyPath
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='add_surveypath'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='change_surveypath'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='delete_surveypath'))

        # SurveyResponse
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='add_surveyresponse'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='change_surveyresponse'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='delete_surveyresponse'))

        # HealthStateRating
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='add_healthstaterating'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='change_healthstaterating'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='delete_healthstaterating'))

        # Users
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='add_user'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='change_user'))
        super_admin_group.permissions.add(orm['auth.permission'].objects.get(codename='delete_user'))


        # Survey Admins
        # Most people administering the survey.
        admin_group = orm['auth.group'].objects.get_or_create(name="Survey Administrators")[0]

        les = orm['auth.user'].objects.get_or_create(
            username="llenert",
            email="leslie.lenert@gmail.com",
            first_name="Leslie",
            last_name="Lenert",
            is_staff=True,
        )[0]
        les.save()

        les.groups.add(super_admin_group)
        les.groups.add(admin_group)

        admin = orm['auth.user'].objects.get_or_create(
            username="admin",
            first_name="General",
            last_name="Admin",
            is_staff=True,
        )[0]
        admin.save()
        admin.groups.add(admin_group)


    def backwards(self, orm):
        super_admin_group = orm['auth.group'].objects.get_or_create(name="Survey Super-Admins")[0]
        super_admin_group.delete()
        admin_group = orm['auth.group'].objects.get_or_create(name="Survey Administrators")[0]
        admin_group.delete()
        les = orm['auth.user'].objects.get_or_create(username="llenert")[0]
        les.delete()



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
            'health_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.HealthState']"}),
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

    complete_apps = ['auth', 'survey']
    symmetrical = True
