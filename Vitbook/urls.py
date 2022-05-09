from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from Vitbook import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),                 
    path('', include('social.urls')), 
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



