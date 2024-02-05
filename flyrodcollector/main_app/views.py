from .models import Flyrod, Flyreel
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
    return render(request, 'flyrods/rod_detail.html', {'flyrod': flyrod})

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