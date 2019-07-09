from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from.import views
from django.views.generic import ListView, DetailView
from ase_site.req.models import SendRequest

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=SendRequest.objects.all().order_by("-date")[:20],template_name="ase_site/req/templates/posts.html")),
    # url(r'^$', views.ViewAllRequests.as_view()),
    url(r'create/',views.CreateRequest),
    url(r'^(?P<pk>\d+)/$',DetailView.as_view(model=SendRequest,template_name ="ase_site/req/templates/post.html")),
    # url(r'^(\d+)/approve',views.approve, name='approve'),
    # url(r'^(\d+)/disapprove',views.disapprove, name='disapprove'),
]
