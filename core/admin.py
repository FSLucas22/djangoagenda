from django.contrib import admin
from core import models


# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo',)


admin.site.register(models.Evento, EventoAdmin)
