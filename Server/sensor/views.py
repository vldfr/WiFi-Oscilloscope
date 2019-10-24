from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


# Create your views here.
def index(request):
    return render(request, 'sensor/index.html', {})


def base(request, base_name):
    return render(request, 'sensor/base.html', {
        'base_name_json': mark_safe(json.dumps(base_name))
    })
