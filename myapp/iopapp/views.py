# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import get_current_site
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.conf import settings
from django.shortcuts import render
from iopapp.appform import ApplicationForm, AppSearch
from iopapp.models import AppForm
import urlparse




def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """   
    is_ajax = False
    
    if request.is_ajax():
      is_ajax = True
      
    if request.user.is_authenticated():
      return HttpResponseRedirect( "/" )
      
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            netloc = urlparse.urlparse(redirect_to)[1]

            # Use default setting if redirect_to is empty
            if not redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL

            # Security check -- don't allow redirection to a different
            # host.
            elif netloc and netloc != request.get_host():
                redirect_to = settings.LOGIN_REDIRECT_URL
              
            # Okay, security checks complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
			#COMMENT-11142013: I have to comment out the next two lines because of error
          #  revision.user    = form.get_user()
          #  revision_meta( request, 'Logging-in', "Session" )
            
            if not request.POST.has_key( "stay_signed" ):
              request.session.set_expiry( 0 )
              
            else:
              request.session[ "stay_signed" ] = True

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
	'is_ajax': is_ajax,
    }
    context.update(extra_context or {})
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request, current_app=current_app))

# Parameters: 	Username and Count
# Return type: None
# Description:	A view that instantly creates dummy users.
#
	
def menu(request):
	  return render(request, 'main/menu.html')
	
def newapp(request):
	if request.method == 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect('../viewapp/%i/' % form.pk)
			
			#original version----------
			#appform.save()
			#--------------------------
	else:
		form = ApplicationForm()
	print "Registration Form objects", (AppForm.objects.all())
           
	
	return render(request, 'newapp/createapp.html', {
		'form':form
	},
	context_instance=RequestContext(request)
	)
	
def viewapp(request, id):
	form = get_object_or_404(AppForm, pk=id)
	
#	if request.method == 'POST':
#		return HttpResponseRedirect('submitform/%i/' % form.pk)
#	else:
	return render(request, 'newapp/doneapp.html', {
		'appform':form,
		'id' : id,
	}
	)

#************************NOV 21 '13 CODE v2*********************
#	form = appform.ModelMultipleChoiceField(queryset=AppForm.objects.all())
#	return render_to_response('doneapp.html', locals(),context_instance=RequestContext(request))
#*****************************END CODE**************************
	
	
#************************NOV 21 '13 CODE v1*********************
#	form = get_object_or_404(AppForm, pk=appform_id)
#	return render_response(
#		  request,
#		  template_index + 'doneapp.html',
#		  {
#		    'appform' : appform,
#	    'appform_id' : appform_id,
#		  }
#	)
#*****************************END CODE**************************


#************************NOV 21 '13 CODE v2*********************
# form = get_object_or_404(AppForm)
#   form = ApplicationForm(request.GET)
#   if form.is_valid():
#    
#	search_query = form.cleaned_data
#	
#  return render(request, 'newapp/doneapp.html')
#*****************************END CODE**************************

#************************NOV 21 '13 CODE v4*********************
#*****************************END CODE**************************
def updateapp(request, id):

	form = get_object_or_404(AppForm, pk=id)
	if request.method == 'POST':
		form_new = ApplicationForm(request.POST, instance=form)
		
		print "Form errors: " + str(form_new.errors);
		
		if form_new.is_valid():
		
#			form_update = form_new.save(commit=False)
			form_new.is_active = True
			form_new.save()
		return HttpResponseRedirect('/iopapp/viewapp/%i/' % form.pk)
			
			#original version----------
			#appform.save()
			#--------------------------
	else:
		form = ApplicationForm(instance=form)
#		form_errors = form_new.errors
           
	
	return render(request, 'newapp/editapp.html', {
		'form':form
	},
	context_instance=RequestContext(request)
	)
	
def submitform(request, id):
	form = get_object_or_404(AppForm, pk=id)
	
	return render(request, 'newapp/submitapp.html', {
		'appform':form,
		'id' : id,
	}
	)
	
def printform(request):
	return HttpResponse("This page is for the report")
	
def searchview(request):

#------------------------------------------------------------------------
#	if 'q' in request.GET and request.GET:
#		q = request.GET['q']
#		appform = AppForm.objects.filter(form_no__icontains = q)
#------------------------------------------------------------------------		
	q, r, s, t = "", "", "", ""
	appform = AppForm.objects.filter()
		
	if 'q' in request.GET and request.GET:
		q = request.GET['q']
		appform = appform.filter(form_no__icontains=q)
	
	if 'r' in request.GET and request.GET:
		r = request.GET['r']
		appform = appform.filter(last_name__icontains=r)

	if 's' in request.GET and request.GET:
		s = request.GET['s']
		appform = appform.filter(first_name__icontains=s)
			
	if 't' in request.GET and request.GET:
		t = request.GET['t']
		appform = appform.filter(middle_name__icontains=t)
	
		return render_to_response('newapp/searchapp.html', {'appform': appform, 'query': q, 'last_name': r, 'first_name': s, 'middle_name': t})
	else:
		return render_to_response('newapp/searchapp.html', {'error': True})
#***************************************
#(request, form_class=AppForm,
#	template_name='newapp/searchapp.html'):
#	form = None
#	if request.method == 'POST':
#		#do search
#		form = form_class(request.POST)
#		if form.is_calid():
#			results = search(form.cleaned_data)
#			if results:
#				return render_to_response(template_name, {'form':
#	form, 'issues': results})
#	else:
#		form = form_class()
#	return render_to_response(template_name, {'form':form})
#***************************************

#*****************NOV 22 '13 CODE v4*************************
#	if request.GET:
#		form_no = request.GET['form_no']
#		results = ModelToSearch.objects.filter(field_istartswith=form_no)
#		return render_to_response('newapp/searchapp.html', {'results': results})
#	return render_to_response('newapp/searchapp.html', {})
#***********************END CODE******************************

#*****************NOV 22 '13 CODE v3*************************
#	if request.method == 'POST':
#		results = AppForm.objects.all()
#		
#		form_no = request.POST.get('form_no', None)
#		if form_no:
#			results = results.filter(form_no=form_no)
#			
#		last_name = request.POST.get('last_name', None)
#		if last_name:
#			results = results.filter(last_name=last_name)
#		
#		first_name = request.POST.get('first_name', None)
#		if first_name:
#			results = results.filter(first_name=first_name)
#			
#		middle_name = request.POST.get('middle_name', None)
#		if middle_name:
#			results = results.filter(middle_name=middle_name)
#		return render_to_response('searchapp.html', {'appform': AppSearch(request.POST), 'appform': results})
#
#		return render_to_response('searchapp.html', {'appform': AppSearch()})
#***********************END CODE******************************


#*****************NOV 22 '13 CODE v2*************************
#	if isinstance(keywords, str):
#		keywords = [keywords]
#	if not isinstance(keywords, list):
#		return None
#	
#	list_form_qs = [Q(form_no__icontains=x) for x in keywords]
#	list_last_qs = [Q(last_name__icontains=x) for x in keywords]
#	list_first_qs = [Q(first_name__icontains=x) for x in keywords]
#	list_middle_qs = [Q(middle_name__icontains=x) for x in keywords]
#	final_q = reduce(operator.or_, list_form_qs + list_last_qs + list_first_qs + list_middle_qs)
#	r_qs = appform.filter(final_q)
#	return r_qs
#***********************END CODE******************************

#*****************NOV 22 '13 CODE v1**************************
#	if request.method == 'POST':
#		form = ApplicationForm(request.POST)
#		if form.is_valid():
#		
#			return HttpResponseRedirect(reverse(
#              'menu',
#              args=[])
#	  )
#	
#	else:
#		form = ApplicationForm()
#	
#	return render(request, 'newapp/searchapp.html', {
#		'form':form,
#	}
#	)
#***********************END CODE******************************
	
