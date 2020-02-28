from django.urls import path

from . import views

urlpatterns = [
    path('get', views.get_data, name='get_gps_data'),
    path('post', views.post_data, name='post_gps_data'),
]
