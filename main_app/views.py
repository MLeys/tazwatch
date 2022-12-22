from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


class Taz:
  def __init__(self, name, sex, location, age, note, image):
    self.name = name
    self.sex = sex
    self.location = location
    self.age = age
    self.note = note
    self.image = image


tazs = [
  Taz('Taz', 'male', 'Tazmania', -1,'WILD and CRAZY! This guy spins like a hurricane and literally tears EVERYTHING APART! Soooooo destructive, would not reccomend as pet', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Taz-Looney_Tunes.svg/1200px-Taz-Looney_Tunes.svg.png'),
  Taz('Urkle', 'male', 'San Diego Zoo', 4, 'Cute little guy', 'https://cdn1.gttwl.net/attachments/Screen_Shot_2019_04_22_at_9_14_06_PM_63723201298112817.png?w=1024&h=768&fit=crop&crop=entropy&auto=format,enhance&q=60'),
  Taz('Clementine', 'female', "San Diego Zoo", 2, 'pregnant and aggresive', 'https://science.sandiegozoo.org/sites/default/files/blogimages/T13_0703_035.jpg'),

]
        
    









# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def taz_index(request):
    return render(request, 'tazs/index.html', {'tazs': tazs})

