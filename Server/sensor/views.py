from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.http import HttpResponse
import json

from .models import SensorData, Sensor


# Create your views here.
def home(request):
    template_name = "index.html"
    context = {"title": "Home",
               "section_title": "Values",
               "sensor_data": SensorData.objects.filter(sensor__name="Sensor1")}
    get_obj = get_template(template_name)
    rendered_template = get_obj.render(context)
    return HttpResponse(rendered_template)


def about(request):
    pass
