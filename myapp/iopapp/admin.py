from django.contrib import admin
from iopapp.models import AppForm

class AppFormAdmin(admin.ModelAdmin):
	fieldsets = [
	('Personal Information', {'fields': ['last_name', 
					'first_name', 'middle_name', 'birth_date','birth_place',
					'sex', 'civil_status', 'residence_address', 'nationality', 
					'contact_number', 'sss_gsis', 'tin', 'name_eac',
					'occup_position', 'date_empmem', 'term_loan', 'amount_loan']} ),
	('Statement of Health', {'fields': ['reason', 'reason_details', 
					'height', 'weight']}),
	('General Health Information', {'fields': ['question1', 'detail_q1', 
					'question2', 'detail_q2']}),
	('Personal Health Information', {'fields': ['question3', 'detail_q3', 
					'question4', 'detail_q4','question5a', 'detail_q5a', 
					'question5b', 'detail_q5b', 'question5c', 'detail_q5c',
					'question5d', 'detail_q5d', 'question6', 'detail_q6']}),
	]
	
admin.site.register(AppForm, AppFormAdmin)
