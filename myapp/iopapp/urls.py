from django.conf.urls import patterns, url

from iopapp import views

urlpatterns = patterns('',
	url(r'^menu/$', views.menu, name='menu'),
	url(r'^$', views.login, name='login'),
	url(r'^newapp/$', views.newapp, name='newapp'), #COMMENT 11142013 : just added "menu/"
	url(r'^viewapp/(?P<id>\d+)/$', views.viewapp, name='viewapp'),
#	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^updateapp/(?P<id>\d+)/$', views.updateapp, name='updateapp'),
	url(r'^submitform/(?P<id>\d+)/$', views.submitform, name='submitform'),
	url(r'^printform/$', views.printform, name='printform'),
	url(r'^searchview/$', views.searchview, name='searchview'),
	)