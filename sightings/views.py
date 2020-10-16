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
