# twata/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^graph/$', views.GraphPageView.as_view(), name='graph'),
]
