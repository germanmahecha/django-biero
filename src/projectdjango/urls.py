from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^ajouter/', 'biero.views.ajouter', name='ajouter'),
	url(r'^', include('biero.urls'))
	
    
]

                          
                          