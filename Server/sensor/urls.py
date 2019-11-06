# sensor/urls.py
from django.conf.urls import url
from django.urls import path

from .views import home, about, groups, reading

urlpatterns = [
    url("home/", home),
    url("groups/", groups),
    path("reading/<id>/", reading)
    # path("/", about)
]
