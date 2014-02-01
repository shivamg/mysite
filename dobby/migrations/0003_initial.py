# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('dirtydb', (
            ('prodid', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True, db_column='prodId')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='name', blank=True)),
            ('sitename', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='siteName', blank=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='sku', blank=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='desc', blank=True)),
            ('href', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='href', blank=True)),
            ('imghref', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='imgHref', blank=True)),
            ('origprice', self.gf('django.db.models.fields.FloatField')(db_column='origPrice', blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(db_column='price', blank=True)),
            ('category', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='category', blank=True)),
            ('tag', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='tag', blank=True)),
            ('landingpage', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='landingPage', blank=True)),
            ('landingroot', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='landingRoot', blank=True)),
            ('landingcount', self.gf('django.db.models.fields.IntegerField')(max_length=255, db_column='landingCount', blank=True)),
            ('features', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='features', blank=True)),
            ('delivery', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='delivery', blank=True)),
            ('emi', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='emi', blank=True)),
            ('sizes', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='sizes', blank=True)),
            ('brand', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='brand', blank=True)),
            ('color', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='color', blank=True)),
            ('owncat', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, db_column='ownCat', blank=True)),
        ))
        db.send_create_signal(u'dobby', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('dirtydb')


    models = {
        u'dobby.product': {
            'Meta': {'object_name': 'Product', 'db_table': "'dirtydb'"},
            'brand': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'brand'", 'blank': 'True'}),
            'category': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'category'", 'blank': 'True'}),
            'color': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'color'", 'blank': 'True'}),
            'delivery': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'delivery'", 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'desc'", 'blank': 'True'}),
            'emi': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'emi'", 'blank': 'True'}),
            'features': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'features'", 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'href'", 'blank': 'True'}),
            'imghref': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'imgHref'", 'blank': 'True'}),
            'landingcount': ('django.db.models.fields.IntegerField', [], {'max_length': '255', 'db_column': "'landingCount'", 'blank': 'True'}),
            'landingpage': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'landingPage'", 'blank': 'True'}),
            'landingroot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'landingRoot'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'name'", 'blank': 'True'}),
            'origprice': ('django.db.models.fields.FloatField', [], {'db_column': "'origPrice'", 'blank': 'True'}),
            'owncat': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'ownCat'", 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'db_column': "'price'", 'blank': 'True'}),
            'prodid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True', 'db_column': "'prodId'"}),
            'sitename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'siteName'", 'blank': 'True'}),
            'sizes': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'sizes'", 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'sku'", 'blank': 'True'}),
            'tag': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'db_column': "'tag'", 'blank': 'True'})
        }
    }

    complete_apps = ['dobby']