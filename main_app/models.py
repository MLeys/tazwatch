from django.db import models
from django.urls import reverse

class Taz(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    note = models.TextField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/images/')



        ## This handles REDIRECTS FOR OUR CBV's
    def get_absolute_url(self):
        # first argument is a name of a url (looks at kwargs) . . . 
        # self.id is referring to the id of the cat ou just crreated or updated
        return reverse('detail', kwargs={'taz_id': self.id})


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
	date = models.DateField('Feeding Date')
	meal = models.CharField(
		max_length=1,
		choices=MEALS, 
		default=MEALS[0][0])

	taz = models.ForeignKey(Taz, on_delete=models.CASCADE)
	
	def __str__(self):

		return f"{self.get_meal_display()} on {self.date}"
	class Meta:
		ordering = ['date']
