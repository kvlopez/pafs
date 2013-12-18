# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AppForm.currency'
        db.add_column(u'iopapp_appform', 'currency',
                      self.gf('django.db.models.fields.CharField')(default='PHP', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AppForm.currency'
        db.delete_column(u'iopapp_appform', 'currency')


    models = {
        u'iopapp.appform': {
            'Meta': {'object_name': 'AppForm'},
            'amount_loan': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'birth_place': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'civil_status': ('django.db.models.fields.CharField', [], {'default': "'Single'", 'max_length': '10'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'PHP'", 'max_length': '10'}),
            'date_apply': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_empmem': ('django.db.models.fields.DateField', [], {}),
            'date_occur_5a': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_occur_5b': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_occur_5c': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_occur_5d': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_occur_6': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'detail_q1': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q2': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q3': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q4': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q5a': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q5b': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q5c': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q5d': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'detail_q6': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'diagnosis_5a': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'diagnosis_5b': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'diagnosis_5c': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'diagnosis_5d': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'diagnosis_6': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'doctor_5a': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '100'}),
            'doctor_5b': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '100'}),
            'doctor_5c': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '100'}),
            'doctor_5d': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '100'}),
            'doctor_6': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'form_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'hospital_name_5a': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'hospital_name_5b': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'hospital_name_5c': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'hospital_name_5d': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'hospital_name_6': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_comp': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '100'}),
            'lab_test_5a': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'lab_test_5b': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'lab_test_5c': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'lab_test_5d': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'lab_test_6': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_eac': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nationality': ('django.db.models.fields.CharField', [], {'default': "'Filipino'", 'max_length': '50'}),
            'occup_position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.IntegerField', [], {}),
            'policy_amt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'present_cond_5a': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'present_cond_5b': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'present_cond_5c': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'present_cond_5d': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'present_cond_6': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
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
            'reason_rpr': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'residence_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'results_medtest_5a': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'results_medtest_5b': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'results_medtest_5c': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'results_medtest_5d': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'results_medtest_6': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '250'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'sss_gsis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'term_loan': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tin': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['iopapp']