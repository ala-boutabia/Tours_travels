from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.index),
    path('tours/<slug:tour_slug>', views.tour_detail, name='tour-detail')
]