from.import views
from django.urls import path

urlpatterns = [
    path('get', views.get_data, name='get_gps_data'),
    path('post', views.post_data, name='post_gps_data'),
]
