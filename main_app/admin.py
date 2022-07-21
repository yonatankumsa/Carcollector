from django.contrib import admin

# Register your models here.
from .models import Car,Mods,Shop

# Register your models here
admin.site.register(Car)
admin.site.register(Mods)
admin.site.register(Shop)
