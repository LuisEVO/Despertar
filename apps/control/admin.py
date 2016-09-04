from django.contrib import admin
from .models import *


class MarcacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'hora')

admin.site.register(Marcacion, MarcacionAdmin)
