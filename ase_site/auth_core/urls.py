from django.conf.urls import url
from django.views.generic import ListView, DetailView

from . import views
from .models import User

urlpatterns = [
    url(r'login/', views.login_view, name='login'),
    url(r'logout/', views.logout_view, name="logout"),
    url(r'register/', views.register_view, name="register"),
    url(r'users/', ListView.as_view(
        queryset=User.objects.all().order_by("last_name").order_by("first_name").filter(is_admin=False),
        template_name="ase_site/auth_core/templates/users.html"))
]
