from django.conf.urls import path,include
from django.urls import path, include
from . import views
from django.contrib.auth import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/$', views.logout, {"next_page": '/'}),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    
]