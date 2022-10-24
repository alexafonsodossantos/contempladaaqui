from django.contrib import admin

# Register your models here.

from .models import Cota, Parcelas, Imagem

admin.site.register(Cota)
admin.site.register(Parcelas)
admin.site.register(Imagem)