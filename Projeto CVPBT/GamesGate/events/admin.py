from django.contrib import admin
from .models import Categorie, Localizacao, Campo, Reserva
# Register your models here.

admin.site.register(Categorie)
admin.site.register(Localizacao)
admin.site.register(Campo)
admin.site.register(Reserva)