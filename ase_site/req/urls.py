from django.urls import path
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from ase_site.data.models import Application

from. import views


urlpatterns = [
    # url(r'all/', ListView.as_view(
    #     queryset=Application.objects.all().order_by("-delivery_date")[:20],
    #     template_name="ase_site/req/templates/posts.html")
    #     ),
    path('all/', views.show_all_applications),
    path('all/<str:material_filter>/<str:status_filter>', views.show_all_applications),
    url(r'create/concrete', views.create_beton_request),
    url(r'create/sand', views.create_sand_request),
    url(r'create/PGS', views.create_PGS_request),
    # url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Application, template_name ="ase_site/req/templates/post.html",)),
    path('<int:id_>/', views.show_application, name='show_app'),
    path('<int:id_>/print/', views.create_word),
    path('<int:id_>/approve/', views.approve),
    path('all/<str:material_filter>/<str:status_filter>/<str:sort_field>/<str:sort_type>', views.show_all_applications),
    path('map/<str:mp>', views.show_all_applications),
    path('xlsx/<str:material_filter>/<str:status_filter>', views.create_excel)
]
