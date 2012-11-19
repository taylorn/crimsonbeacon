# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Case.title'
        db.add_column('case_case', 'title',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 11, 15, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'Case.subtitle'
        db.add_column('case_case', 'subtitle',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Case.body'
        db.add_column('case_case', 'body',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Case.link'
        db.add_column('case_case', 'link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Case.link_display_method'
        db.add_column('case_case', 'link_display_method',
                      self.gf('django.db.models.fields.CharField')(default='embedded', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Case.title'
        db.delete_column('case_case', 'title')

        # Deleting field 'Case.subtitle'
        db.delete_column('case_case', 'subtitle')

        # Deleting field 'Case.body'
        db.delete_column('case_case', 'body')

        # Deleting field 'Case.link'
        db.delete_column('case_case', 'link')

        # Deleting field 'Case.link_display_method'
        db.delete_column('case_case', 'link_display_method')


    models = {
        'case.case': {
            'Meta': {'object_name': 'Case'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_display_method': ('django.db.models.fields.CharField', [], {'default': "'embedded'", 'max_length': '8'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['case']