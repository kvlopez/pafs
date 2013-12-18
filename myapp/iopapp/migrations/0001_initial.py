# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AppForm'
        db.create_table(u'iopapp_appform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_no', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('birth_place', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('civil_status', self.gf('django.db.models.fields.CharField')(default='Single', max_length=10)),
            ('residence_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nationality', self.gf('django.db.models.fields.CharField')(default='Filipino', max_length=50)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('sss_gsis', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('tin', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('name_eac', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('occup_position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_empmem', self.gf('django.db.models.fields.DateField')()),
            ('term_loan', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('amount_loan', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=2)),
            ('reason', self.gf('django.db.models.fields.CharField')(default='Over NEL', max_length=45)),
            ('reason_details', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('question1', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q1', self.gf('django.db.models.fields.TextField')()),
            ('question2', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q2', self.gf('django.db.models.fields.TextField')()),
            ('question3', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q3', self.gf('django.db.models.fields.TextField')()),
            ('question4', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q4', self.gf('django.db.models.fields.TextField')()),
            ('question5a', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q5a', self.gf('django.db.models.fields.TextField')()),
            ('question5b', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q5b', self.gf('django.db.models.fields.TextField')()),
            ('question5c', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q5c', self.gf('django.db.models.fields.TextField')()),
            ('question5d', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q5d', self.gf('django.db.models.fields.TextField')()),
            ('question6', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('detail_q6', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'iopapp', ['AppForm'])


    def backwards(self, orm):
        # Deleting model 'AppForm'
        db.delete_table(u'iopapp_appform')


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