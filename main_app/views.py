from django.shortcuts import render

# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Taz


# class TazUpdate(UpdateView):
#   model = Taz
class TazUpdate(UpdateView):
  model = Taz
  fields = [ 'sex', 'location', 'age', 'note', 'image']

class TazDelete(DeleteView):
  model = Taz
  success_url = '/tazs/'
  



class TazCreate(CreateView):
  model = Taz
  # fields = ['name', 'sex', 'location', 'age', 'note']
  fields = '__all__'

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


