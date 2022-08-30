from django.contrib import admin

# Register your models here.

from .models import Cota, Administradora

admin.site.register(Cota)
admin.site.register(Administradora)