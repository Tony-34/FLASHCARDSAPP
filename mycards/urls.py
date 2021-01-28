from django.conf.urls import url
from . import views
from django.contrib.auth import views 


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    
]