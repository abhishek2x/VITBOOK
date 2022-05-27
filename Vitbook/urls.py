from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from Vitbook import settings

urlpatterns = [
    path('', include('social.urls')), 
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),      
    path('__debug__/', include('debug_toolbar.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



