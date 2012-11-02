# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Case'
        db.create_table('case_case', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('case', ['Case'])


    def backwards(self, orm):
        # Deleting model 'Case'
        db.delete_table('case_case')


    models = {
        'case.case': {
            'Meta': {'object_name': 'Case'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['case']