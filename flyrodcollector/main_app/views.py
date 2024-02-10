from .models import Flyrod, Flyreel
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TripForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def flyrods_index(request):
    flyrods = Flyrod.objects.all()
    return render(request, 'flyrods/index.html', { 'flyrods': flyrods })

def flyreels_index(request):
    flyreels = Flyreel.objects.all()
    return render(request, 'flyreels/index.html', { 'flyreels': flyreels })

def rod_detail(request, flyrod_id):
    flyrod = Flyrod.objects.get(id=flyrod_id)
    trip_form = TripForm()
    return render(request, 'flyrods/rod_detail.html', {'flyrod': flyrod, 'trip_form': trip_form})

def reel_detail(request, flyreel_id):
    flyreel = Flyreel.objects.get(id=flyreel_id)
    return render(request, 'flyreels/reel_detail.html', {'flyreel': flyreel})

class RodCreate(CreateView):
    model= Flyrod
    fields = '__all__'

class RodUpdate(UpdateView):
    model = Flyrod
    fields = '__all__'

class RodDelete(DeleteView):
    model = Flyrod
    success_url = '/flyrods/'

class ReelCreate(CreateView):
    model= Flyreel
    fields = '__all__'

class ReelUpdate(UpdateView):
    model = Flyreel
    fields = '__all__'

class ReelDelete(DeleteView):
    model = Flyreel
    success_url = '/flyrods/'

def add_trip(request, flyrod_id):
  form = TripForm(request.POST)
  if form.is_valid():
    new_trip = form.save(commit=False)
    new_trip.flyrod_id = flyrod_id
    new_trip.save()
  return redirect('rod_detail', flyrod_id=flyrod_id)