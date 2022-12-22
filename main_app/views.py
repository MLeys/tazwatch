from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Taz


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tazs_index(request):
  tazs = Taz.objects.all()
  return render(request, 'tazs/index.html', {'tazs': tazs})

def tazs_detail(request, taz_id):
  taz = Taz.objects.get(id=taz_id)
  return render(request, 'tazs/detail.html', {'taz': taz})


