from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse

from .models import Squirrel
from .forms import SquirrelForm

# Create your views here.

def index(request):
    squirrels = Squirrel.objects.order_by('Unique_Squirrel_ID')
    context = {'sightings' : squirrels}
    return render(request, 'sightings/index.html',context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form=SquirrelForm()
    context ={'form':form}
    return render(request,'sightings/add.html',context)

def edit(request, squirrel_ID):
    sighting = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_ID)
    if request.method=='POST':
        form=SquirrelForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_ID}')
    else:
        form = SquirrelForm(instance=sighting)
    context ={
            'sighting':sighting,
            'form':form
    }
    return render(request, 'sightings/edit.html', context)

