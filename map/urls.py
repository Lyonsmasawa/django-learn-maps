from django.urls import path                                                                                                               
from . import views

urlpatterns = [ 
    # url(r'', views.default_map, name="default"),
    path('', views.calculate_distance_view, name='calculate-view'),
]