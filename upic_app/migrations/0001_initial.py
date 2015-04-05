# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'upic_app_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lat', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('long', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'upic_app', ['Place'])

        # Adding model 'Tweets'
        db.create_table(u'upic_app_tweets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('post_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user_image', self.gf('django.db.models.fields.URLField')(default='', max_length=200)),
            ('tweet_image', self.gf('django.db.models.fields.URLField')(default='', max_length=200)),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['upic_app.Place'])),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'upic_app', ['Tweets'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'upic_app_place')

        # Deleting model 'Tweets'
        db.delete_table(u'upic_app_tweets')


    models = {
        u'upic_app.place': {
            'Meta': {'object_name': 'Place'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'long': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'place_id': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'upic_app.tweets': {
            'Meta': {'object_name': 'Tweets'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['upic_app.Place']"}),
            'post_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {}),
            'tweet_image': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_image': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['upic_app']