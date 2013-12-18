from django.db import models

# Create your models here.

class AppForm(models.Model):
	form_no = models.CharField(max_length=100)
	last_name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	birth_date = models.DateField()
	birth_place = models.CharField(max_length=100)
	page = models.IntegerField()
	#choices for sex
	male = 'M'
	female = 'F'
	#assign variables for each option
	sex_choices = (
		(male, 'M'),
		(female, 'F'),
	)
	#do the selection 
	sex = models.CharField(max_length=1, choices=sex_choices, default=male)
	#choices for civil status
	single = 'Single'
	married = 'Married'
	widowed = 'Widowed'
	#assign variable for each option
	civil_status_choices = (
		(single, 'Single'),
		(married, 'Married'), 
		(widowed, 'Widowed'),
	)
	civil_status = models.CharField(max_length=10, choices=civil_status_choices, 
	default=single)
	residence_address = models.CharField( max_length=100)
	nationality = models.CharField(max_length=50, default="Filipino")
	contact_number = models.CharField(max_length=45)
	sss_gsis = models.CharField( max_length=50, null=True)
	tin = models.CharField(max_length=50, null=True)
	name_eac = models.CharField(max_length=200)
	occup_position = models.CharField(max_length=100)
	date_empmem = models.DateField()
	term_loan = models.IntegerField(null=True)
	amount_loan = models.DecimalField( max_digits=19, decimal_places=2, null=True)
	# choices for term loan
	year='year'
	month='month'
	
	#assign variable
	term_choices = (
		(year, 'year'),
		(month, 'month'),
	)
	
	term_loan_d = models.CharField(max_length=10, choices=term_choices, default=year)
	
	#choices for currency
	php='PHP'
	usd='USD'
	#assign variable for each currency
	curr_choices = (
		(php, 'PHP'),
		(usd, 'USD'),
)
	currency = models.CharField(max_length=10, choices=curr_choices, default=php)
# ########################################################################################
	#choices for reason
	nel = 'Over NEL'
	age = 'Over Age Limit'
	enrol = 'Late Enrollment'
	state = 'Reinstatement'
	others = 'Others'
	#assign variable
	reason_choices = (
		(nel, 'Over NEL'),
		(age, 'Over Age Limit'),
		(enrol, 'Late Enrolment'),
		(state, 'Reinstatement'),
		(others, 'Others'),
	)
	reason = models.CharField(max_length=45, choices=reason_choices, default=nel)
	reason_details = models.CharField(max_length=100, default=' ')
	height = models.CharField(max_length=10, null=True)
	weight = models.CharField(max_length=10, null=True)
	
	#choices for question
	yes = 'Yes'
	no = 'No'
	qchoices = (
		(yes, 'Yes'),
		(no, 'No'), 
	)
	# General Health Information
	question1 = models.CharField(max_length=3, choices=qchoices)
	detail_q1 = models.TextField(default=' ')
	question2 = models.CharField(max_length=3, choices=qchoices)
	detail_q2 = models.TextField(default=' ')
	# Personal Health Information
	question3 = models.CharField(max_length=3, choices=qchoices)
	detail_q3 = models.TextField(default=' ')
	question4 = models.CharField(max_length=3, choices=qchoices)
	detail_q4 = models.TextField(default=' ')
	question5a = models.CharField(max_length=3, choices=qchoices)
	detail_q5a = models.TextField(default=' ')
	question5b = models.CharField(max_length=3, choices=qchoices)
	detail_q5b = models.TextField(default=' ')
	question5c = models.CharField(max_length=3, choices=qchoices)
	detail_q5c = models.TextField(default=' ')
	question5d = models.CharField(max_length=3, choices=qchoices)
	detail_q5d = models.TextField(default=' ')
	question6 = models.CharField(max_length=3, choices=qchoices)
	detail_q6 = models.TextField(default=' ')
	
	# ****************** additional fields ******************* #
	#********************DATE ADDED********************#
	#--------------------------12.09.2013--------------------------#
	
	# These are the table fields for question number 3
	date_apply = models.DateField(null=True)
	insurance_comp = models.CharField(max_length=100, default=' ')
	policy_amt = models.DecimalField(max_digits=19, decimal_places=2, null=True)
	reason_rpr = models.CharField(max_length=250, default=' ')
	
	# These are the fields for question 5a t 5d and 6
	date_occur_5a = models.DateField(null=True)
	diagnosis_5a = models.CharField(max_length=250, default=' ')
	doctor_5a = models.CharField(max_length=100, default=' ')
	hospital_name_5a = models.CharField(max_length=250, default=' ')
	lab_test_5a = models.CharField(max_length=250, default=' ')
	results_medtest_5a = models.CharField(max_length=250, default=' ')
	present_cond_5a = models.CharField(max_length=250, default=' ')
	
	date_occur_5b = models.DateField(null=True)
	diagnosis_5b = models.CharField(max_length=250, default=' ')
	doctor_5b = models.CharField(max_length=100, default=' ')
	hospital_name_5b = models.CharField(max_length=250, default=' ')
	lab_test_5b = models.CharField(max_length=250, default=' ')
	results_medtest_5b = models.CharField(max_length=250, default=' ')
	present_cond_5b = models.CharField(max_length=250, default=' ')
	
	date_occur_5c = models.DateField(null=True)
	diagnosis_5c = models.CharField(max_length=250, default=' ')
	doctor_5c = models.CharField(max_length=100, default=' ')
	hospital_name_5c = models.CharField(max_length=250, default=' ')
	lab_test_5c = models.CharField(max_length=250, default=' ')
	results_medtest_5c = models.CharField(max_length=250, default=' ')
	present_cond_5c = models.CharField(max_length=250, default=' ')
	
	date_occur_5d = models.DateField(null=True)
	diagnosis_5d	= models.CharField(max_length=250, default=' ')
	doctor_5d = models.CharField(max_length=100, default=' ')
	hospital_name_5d = models.CharField(max_length=250, default=' ')
	lab_test_5d = models.CharField(max_length=250, default=' ')
	results_medtest_5d = models.CharField(max_length=250, default=' ')
	present_cond_5d = models.CharField(max_length=250, default=' ')

	date_occur_6 = models.DateField(null=True)
	diagnosis_6 = models.CharField(max_length=250, default=' ')
	doctor_6 = models.CharField(max_length=100, default=' ')
	hospital_name_6 = models.CharField(max_length=250, default=' ')
	lab_test_6 = models.CharField(max_length=250, default=' ')
	results_medtest_6 = models.CharField(max_length=250, default=' ')
	present_cond_6 = models.CharField(max_length=250, default=' ')
	

	