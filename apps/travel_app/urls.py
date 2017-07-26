from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addform$', views.addform),
    url(r'^add$', views.add),
    url(r'^destination/(?P<id>\d+)$', views.destination),
]