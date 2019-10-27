# sensor/urls.py
from django.conf.urls import url

from .views import home, about

urlpatterns = [
    url("home/", home),
    # path("/", about)
]
