# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.title'
        db.add_column('article_article', 'title',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 11, 15, 0, 0), max_length=50),
                      keep_default=False)

        # Adding field 'Article.subtitle'
        db.add_column('article_article', 'subtitle',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Article.body'
        db.add_column('article_article', 'body',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Article.link'
        db.add_column('article_article', 'link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Article.link_display_method'
        db.add_column('article_article', 'link_display_method',
                      self.gf('django.db.models.fields.CharField')(default='embedded', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.title'
        db.delete_column('article_article', 'title')

        # Deleting field 'Article.subtitle'
        db.delete_column('article_article', 'subtitle')

        # Deleting field 'Article.body'
        db.delete_column('article_article', 'body')

        # Deleting field 'Article.link'
        db.delete_column('article_article', 'link')

        # Deleting field 'Article.link_display_method'
        db.delete_column('article_article', 'link_display_method')


    models = {
        'article.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_display_method': ('django.db.models.fields.CharField', [], {'default': "'embedded'", 'max_length': '8'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['article']