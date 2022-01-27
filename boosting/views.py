from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Division, Services

# Create your views here.
def index(request):
    divisions=Division.objects.all()
    return render(request, 'boosting/home.html', {'divisions':divisions})


def division_details(request, division_slug):
    div_object=Division.objects.get(slug=division_slug)
    services=Services.objects.filter(division=div_object)
    context={'div_object':div_object, 'services':services}

    return render(request, 'boosting/div_details.html', context=context)

def services(request, service_name_slug):

    service_object=Services.objects.get(slug=service_name_slug)
    context={'service_object':service_object}
    return render(request, 'boosting/service_details.html', context=context)
