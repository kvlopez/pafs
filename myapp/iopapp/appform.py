from iopapp.models import AppForm
from django import forms
from django.forms import ModelForm
from django.forms import *
from django.forms.widgets import RadioSelect
from django.forms.widgets import DateInput
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.fields.related import *

# ########## I add this choices to test the radio button functionality###################

Q_CHOICES = [['Yes', 'Yes'], ['No', 'No']]
class ApplicationForm( ModelForm ):
    class Meta:
		fields = [ 'id','form_no','last_name', 'first_name', 'middle_name', 'birth_date', 'birth_place',
					'sex', 'civil_status', 'residence_address', 'nationality', 'contact_number',
					'sss_gsis', 'tin', 'name_eac', 'occup_position', 'date_empmem', 'term_loan', 
					'amount_loan', 'reason', 'reason_details', 'height', 'weight', 'question1', 
					'question2', 'question3', 'question4', 'question5a', 'question5b', 'question5c',
					'question5d', 'question6', 'page', 'detail_q1', 'detail_q2', 'detail_q3', 'detail_q4',
					'detail_q5a', 'detail_q5b', 'detail_q5c', 'detail_q5d', 'detail_q6', 'date_apply',
					'insurance_comp', 'policy_amt', 'reason_rpr', 
					'date_occur_5a', 'diagnosis_5a', 'doctor_5a', 'hospital_name_5a', 
					'lab_test_5a', 'results_medtest_5a', 'present_cond_5a', 
					'date_occur_5b', 'diagnosis_5b', 'doctor_5b', 'hospital_name_5b', 
					'lab_test_5b', 'results_medtest_5b', 'present_cond_5b', 
					'date_occur_5c', 'diagnosis_5c', 'doctor_5c', 'hospital_name_5c', 
					'lab_test_5c', 'results_medtest_5c', 'present_cond_5c', 
					'date_occur_5d', 'diagnosis_5d', 'doctor_5d', 'hospital_name_5d', 
					'lab_test_5d', 'results_medtest_5d', 'present_cond_5d', 
					'date_occur_6', 'diagnosis_6', 'doctor_6', 'hospital_name_6', 
					'lab_test_6', 'results_medtest_6', 'present_cond_6', 'currency', 'term_loan_d' ]
	
		birth_date = forms.DateField(widget = AdminDateWidget)
		model = AppForm
		def __init__(self, *args, **kwargs):
			super(AppForm, self).__init__(*args, **kwargs)
			instance = getattr(self, 'instance', None)
			if instance and instance.pk:
				self.fields['nationality'].widget.attrs['readonly'] = True
		
		def clean_nationality(self):
			instance = getattr(self, 'instance', None)
			if instance and instance.pk:
				return instance.nationality
			else: 
				return self.cleaned_data['nationality']
		
	
		
#		first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
#		birth_date  DateField(widgets=forms.DateInput, label=_("Birthdatee")),
		
		
		detail_q1 = forms.CharField(initial="initial")
		question1 = forms.ChoiceField(  
		choices=Q_CHOICES)
		
	
		widgets = {
			 'last_name': TextInput(
			  attrs = {'style': 'width: 200px;'}
			),
			 'first_name': TextInput(
			  attrs = {'style': 'width: 200px;'}
			),
			 'contact_number': TextInput(
			  attrs = {'style': 'width: 200px;'}
			),
			 'residence_address': TextInput(
			  attrs = {'style': 'width: 410px;'}
			),
			 'name_eac': TextInput(
			  attrs = {'style': 'width: 410px;'}
			),
			
			'birth_date': DateInput( format='%m/%d/%Y'), \
			'date_empmem': DateInput( format='%m/%d/%Y'), \
			'question1' : forms.RadioSelect(), \
			'question2' : forms.RadioSelect(), \
			'question3' : forms.RadioSelect(), \
			'question4' : forms.RadioSelect(), \
			'question5a' : forms.RadioSelect(), \
			'question5b' : forms.RadioSelect(), \
			'question5c' : forms.RadioSelect(), \
			'question5d' : forms.RadioSelect(), \
			'question6' : forms.RadioSelect(),\
		}
	
#		fieldsets = [
#		('Personal Information', {'fields': ['last_name', 
#					'first_name', 'middle_name', 'birth_date','birth_place',
#					'sex', 'civil_status', 'residence_address', 'nationality', 
#					'contact_number', 'sss_gsis', 'tin', 'name_eac',
#					'occup_position', 'date_empmem', 'term_loan', 'amount_loan']} ),
#		('Statement of Health', {'fields': ['reason', 'reason_details', 
#					'height', 'weight']}),
#		('General Health Information', {'fields': ['question1', 'detail_q1', 
#					'question2', 'detail_q2']}),
#		('Personal Health Information', {'fields': ['question3', 'detail_q3', 
#					'question4', 'detail_q4','question5a', 'detail_q5a', 
#					'question5b', 'detail_q5b', 'question5c', 'detail_q5c',
#					'question5d', 'detail_q5d', 'question6', 'detail_q6']}),
#		]

class AppSearch(forms.Form):
	form_no = forms.CharField(max_length=200, required=False)
	last_name = forms.CharField(max_length=200)
	first_name = forms.CharField(max_length=200)
	middle_name = forms.CharField(max_length=200)