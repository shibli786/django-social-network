from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,logout_then_login
from django.contrib.auth.views import password_change,password_change_done
from django.contrib.auth.views import password_reset,password_reset_done
from django.contrib.auth.views import password_reset_complete,password_reset_confirm
 




urlpatterns = [




	url(r'^images/$', views.dashboard,name='images'), 
	url(r'^/people/$', views.dashboard,name='people'), 


	url(r'^$', views.dashboard,name='dashboard'), 

    #url(r'^login$', views.user_login,name='login'),
	url(r'^login/$', login,name='login'), 

	url(r'^logout/$',logout,name='logout'),
	url(r'logout-then-login/$',logout_then_login,name='logout-then-login'),

	#password change
		url(r'^password-change/$',password_change,name='password_change'),
		url(r'^password-change-done/$',password_change_done,name='password_change_done'),
	#Password reset
	url(r'^password-reset/$',password_reset,name='password_reset'),
	url(r'^password-reset-done/$',password_reset_done,name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',password_reset_confirm,name='password_reset_confirm'),
	url(r'^password-reset/complete/$',password_reset_complete,name='password_reset_complete'),



]