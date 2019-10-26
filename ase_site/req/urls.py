from django.conf.urls import url
from django.views.generic import ListView, DetailView
from ase_site.data.models import Application

from. import views


urlpatterns = [
    url(r'all/', ListView.as_view(
        queryset=Application.objects.all().order_by("-delivery_date")[:20],
        template_name="ase_site/req/templates/posts.html")
        ),
    url(r'create/concrete', views.create_beton_request),
    url(r'create/sand', views.create_sand_request),
    url(r'create/PGS', views.create_PGS_request),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Application,template_name ="ase_site/req/templates/post.html")),
]
