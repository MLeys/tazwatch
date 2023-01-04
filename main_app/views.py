from django.shortcuts import render, redirect

# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Taz, Restriction
from .forms import FeedingForm
from bootstrap_datepicker_plus.widgets import DatePickerInput

def add_feeding(request, taz_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.taz_id = taz_id
      new_feeding.save()
    return redirect('detail', taz_id=taz_id)


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
  restrictions_taz_doesnt_have = Restriction.objects.exclude(id__in = taz.restrictions.all().values_list('id'))

  feeding_form = FeedingForm()

  return render(request, 'tazs/detail.html', 
    {
      'taz': taz, 
      'feeding_form': feeding_form,
      'restrictions': restrictions_taz_doesnt_have,
    })



class RestrictionList(ListView):
    model = Restriction
    template_name = 'restrictions/index.html'
   
class RestrictionDetail(DetailView):
    model = Restriction
    template_name = 'restrictions/detail.html'
    
class RestrictionCreate(CreateView):
    model = Restriction
    fields = '__all__'

class RestrictionUpdate(UpdateView):
  model = Restriction
  fields = '__all__'

class RestrictionDelete(DeleteView):
  model = Restriction
  success_url = '/restrictions/'
    

def assoc_restriction(request, taz_id, restriction_id):
  # Note that you can pass a restriction's id instead of the whole object
  Taz.objects.get(id=taz_id).restrictions.add(restriction_id)
  return redirect('detail', taz_id=taz_id)


