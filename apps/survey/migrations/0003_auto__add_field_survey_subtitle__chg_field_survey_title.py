# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Survey.subtitle'
        db.add_column('survey_survey', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)


        # Changing field 'Survey.title'
        db.alter_column('survey_survey', 'title', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Deleting field 'Survey.subtitle'
        db.delete_column('survey_survey', 'subtitle')


        # Changing field 'Survey.title'
        db.alter_column('survey_survey', 'title', self.gf('django.db.models.fields.CharField')(max_length=33))

    models = {
        'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['survey']