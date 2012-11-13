# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Survey.link_display_method'
        db.add_column('survey_survey', 'link_display_method',
                      self.gf('django.db.models.fields.CharField')(default='embedded', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Survey.link_display_method'
        db.delete_column('survey_survey', 'link_display_method')


    models = {
        'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_display_method': ('django.db.models.fields.CharField', [], {'default': "'embedded'", 'max_length': '8'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['survey']