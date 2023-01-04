from django.contrib import admin

# import your models here
from .models import Taz, Feeding, Restriction

# Register your models here
admin.site.register(Taz)
admin.site.register(Feeding)
admin.site.register(Restriction)