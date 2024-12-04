from django.urls import path
from . import views



app_name = 'remove_backgorund'



urlpatterns = [
    path('image/', views.remove_background, name='image_remove_background')
]