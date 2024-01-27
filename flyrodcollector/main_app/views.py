from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Wussup! Im a fly fisherman who collects vintage fly rods!<h1>')
