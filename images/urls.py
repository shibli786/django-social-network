from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns=[
url(r'^create/$',views.image_create,name='create'),
url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.image_detail,name='detail'),
url(r'^like/$',views.image_like,name='like'),
url(r'^$',views.image_list,name='list'),
url(r'^users/$',views.user_list,name='user_list'),
url(r'^users.(?P<username>[-\w]+)/$',views.user_detail)


]