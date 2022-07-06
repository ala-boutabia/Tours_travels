from multiprocessing import context
from django.shortcuts import render
from .models import Tour


# Create your views here.

def index(request):
    tours = Tour.objects.all()
    return render(request, 'adventure/index.html', {'tours':tours})

def tour_detail(request, tour_slug):
    selected_tour = Tour.objects.get(slug=tour_slug)
    context = {
        'tour_title': selected_tour.title,
        'tour_description': selected_tour.description,
    }
    return render(request, 'adventure/tour-detail.html', context)

    def __str__(self):
        return self.title


