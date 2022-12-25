from django.forms import ModelForm
from .models import Feeding
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms




class FeedingForm(ModelForm):
	class Meta:
		model = Feeding
		fields = ['date', 'meal']
		widgets = {
			 "date": DatePickerInput(options={"format": "MM/DD/YYYY"}),
			# 'date' : DateInput(),
            # 'time' : TimeInput(), 
		}

