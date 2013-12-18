# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AppForm.page'
        db.delete_column(u'iopapp_appform', 'page')


    def backwards(self, orm):
        # Adding field 'AppForm.page'
        db.add_column(u'iopapp_appform', 'page',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        u'iopapp.appform': {
            'Meta': {'object_name': 'AppForm'},
            'amount_loan': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'birth_place': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'civil_status': ('django.db.models.fields.CharField', [], {'default': "'Single'", 'max_length': '10'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'date_empmem': ('django.db.models.fields.DateField', [], {}),
            'detail_q1': ('django.db.models.fields.TextField', [], {}),
            'detail_q2': ('django.db.models.fields.TextField', [], {}),
            'detail_q3': ('django.db.models.fields.TextField', [], {}),
            'detail_q4': ('django.db.models.fields.TextField', [], {}),
            'detail_q5a': ('django.db.models.fields.TextField', [], {}),
            'detail_q5b': ('django.db.models.fields.TextField', [], {}),
            'detail_q5c': ('django.db.models.fields.TextField', [], {}),
            'detail_q5d': ('django.db.models.fields.TextField', [], {}),
            'detail_q6': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'form_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_eac': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nationality': ('django.db.models.fields.CharField', [], {'default': "'Filipino'", 'max_length': '50'}),
            'occup_position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question1': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question2': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question3': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question5a': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question5b': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question5c': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question5d': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'question6': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'reason': ('django.db.models.fields.CharField', [], {'default': "'Over NEL'", 'max_length': '45'}),
            'reason_details': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'residence_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'sss_gsis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'term_loan': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tin': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['iopapp']