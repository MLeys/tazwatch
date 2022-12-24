from django.contrib import admin

# import your models here
from .models import Taz, Feeding

# Register your models here
admin.site.register(Taz)
admin.site.register(Feeding)