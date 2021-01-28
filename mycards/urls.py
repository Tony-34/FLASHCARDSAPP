from django.conf.urls import path,include
from django.urls import path, include
from . import views
from django.contrib.auth import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/$', views.logout, {"next_page": '/'}),
    path(r'^accounts/', include('registration.backends.simple.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
