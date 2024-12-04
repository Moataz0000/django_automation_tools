from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('dataentry/', include('dataentry.urls', namespace='dataentry')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('emails/', include('emails.urls', namespace='emails')),
    path('remove-background/', include('removebackground.urls', namespace='remove_background')),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)