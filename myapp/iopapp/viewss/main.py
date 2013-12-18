# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import get_current_site
from django.shortcuts import render_to_response
from django.template import RequestContext


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

            revision.user    = form.get_user()
            revision_meta( request, 'Logging-in', "Session" )
            
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

#Parameters: 	Username and Count
#Return type: None
#Description:	A view that instantly creates dummy users.
#
	
def menu(request):
	return HttpResponse("Hello this is the menu page!")
	
def newapp(request):
	return HttpResponse("This page is reserve for application form")
	
def viewapp(request):
	return HttpResponse("This page is for viewing form as clicked DONE")
	
def updateapp(request):
	return HttpResponse("This view is like the new application form but updating only")
	
def submitform(request):
	return HttpResponse("This page is ready for printing")
	
def printform(request):
	return HttpResponse("This page is for the report")
	
def searchview(request):
	return HttpResponse("This page is for searching forms")
	
