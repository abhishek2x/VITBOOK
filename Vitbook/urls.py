from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from Vitbook import settings
from social import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),                 
    path('social/', include('social.urls')), 
    path('', views.welcome.as_view()),            
    # path('accounts/register', views.register, name='register'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
