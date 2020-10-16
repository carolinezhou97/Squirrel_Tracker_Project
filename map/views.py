from django.shortcuts import render
from sightings.models import Squirrel


# Create your views here.

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {'sightings':squirrels}
    return render(request, 'map/index.html', context)
