from django.shortcuts import render, get_object_or_404
from django.template import context
from .models import Measurement

# def default_map(request):
#     # TODO: move this token to Django settings from an environment variable
#     # found in the Mapbox account settings and getting started instructions
#     # see https://www.mapbox.com/account/ under the "Access tokens" section
#     mapbox_access_token = ''
#     return render(request, 'default.html', 
#                   { 'mapbox_access_token': mapbox_access_token })

def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id = 1)

    context = {'distance': obj}

    return render(request, 'map/main.html', context)
