from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurmentsForm
from geopy.geocoders import Nominatim
from .utils import get_geo, get_center_coordinates, get_zoom
from geopy.distance import geodesic
import folium

# def default_map(request):
#     # TODO: move this token to Django settings from an environment variable
#     # found in the Mapbox account settings and getting started instructions
#     # see https://www.mapbox.com/account/ under the "Access tokens" section
#     mapbox_access_token = ''
#     return render(request, 'default.html', 
#                   { 'mapbox_access_token': mapbox_access_token })

def calculate_distance_view(request):
    distance = None
    obj = get_object_or_404(Measurement, id = 3)
    form = MeasurmentsForm(request.POST or None)
    geolocator = Nominatim(user_agent='map')
    destination = None

    ip = '72.14.207.99'
    country, city, lat, lon = get_geo(ip)
    # print('location country', country)
    # print('location city', city)
    # print('location lat, lon', lat, lon)
    location = geolocator.geocode(city) #shortens the response
    # print('###', location)

    # location distance
    l_lat = lat
    l_lon = lon

    pointA = (l_lat, l_lon)

    # innitial folium map
    m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)

    #location marker
    folium.Marker([l_lat, l_lon], tooltip='Click here for more', popup=city['city'],
         icon=folium.Icon(color='purple')).add_to(m)


    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        # print(destination)

        # desitination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat, d_lon)

        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)

        # draw locations

        line = folium.PolyLine(locations=[pointA, pointB], weight = 3, color='blue')
        m.add_child(line)

        #folium map modification
        m = folium.Map(width=800, height=500, location = get_center_coordinates(l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance))

        #destination marker
        folium.Marker([d_lat, d_lon], tooltip='Click here for more', popup=destination,
            icon=folium.Icon(color='red', icon='cloud')).add_to(m)


        instance.location = location
        instance.distance = distance
        instance.save()

    m = m._repr_html_() #html representation


    context = {'distance': distance, 'form': form, 'map': m, 'destination': destination, }

    return render(request, 'map/main.html', context)
