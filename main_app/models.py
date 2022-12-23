from django.db import models
from django.urls import reverse

class Taz(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    note = models.TextField(max_length=250)
    image = models.ImageField()

        ## This handles REDIRECTS FOR OUR CBV's
    def get_absolute_url(self):
        # first argument is a name of a url (looks at kwargs) . . . 
        # self.id is referring to the id of the cat ou just crreated or updated
        return reverse('detail', kwargs={'taz_id': self.id})
