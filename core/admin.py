from django.contrib import admin
from core import models


# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')


admin.site.register(models.Evento, EventoAdmin)
