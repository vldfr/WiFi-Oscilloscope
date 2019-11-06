from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.http import HttpResponse
import json

from .models import SensorData, Sensor, SensorReadingGroup


# Create your views here.
def home(request):
    template_name = "index.html"
    context = {"title": "Home",
               "section_title": "Values",
               "sensor_data": SensorData.objects.filter(group__id=SensorReadingGroup.objects.filter(sensor__name="Sensor1").order_by('-id')[0].id)}
    get_obj = get_template(template_name)
    rendered_template = get_obj.render(context)
    print(request.path)
    return HttpResponse(rendered_template)


def groups(request):
    template_name = "reading_groups.html"
    context = {"title": "Groups",
               "section_title": "Groups",
               "groups": SensorReadingGroup.objects.filter(sensor__name="Sensor1")}
    get_obj = get_template(template_name)
    rendered_template = get_obj.render(context)
    return HttpResponse(rendered_template)


def reading(request, id):
    template_name = "index.html"
    context = {"title": "Reading "+str(id),
               "section_title": "Values",
               "sensor_data": SensorData.objects.filter(group__id=id)}
    get_obj = get_template(template_name)
    rendered_template = get_obj.render(context)
    print(request.path)
    return HttpResponse(rendered_template)

def about(request):
    pass
