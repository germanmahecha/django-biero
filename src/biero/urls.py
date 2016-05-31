from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login

urlpatterns = [
	url(r'^$', 'biero.views.accueil', name='accueil'),
    url(r'^details/(?P<pk>[0-9]+)/$', 'biero.views.details', name='details'),
    url(r'^authentication/', 'biero.views.authentication', name='authentication'),
    url(r'^enregistrement/', 'biero.views.enregistrement', name='enregistrement'),
    url(r'^logout$', auth_views.logout, {'next_page':'/'}, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

