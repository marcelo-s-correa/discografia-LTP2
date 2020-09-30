from django.contrib import admin
from .models import Musica,Banda,Albun

class MusicasAdmin(admin.ModelAdmin):
    lst_adm = [
        'titulo',
        'segundos',
        'album',
        ]

admin.site.register(Musica)
admin.site.register(Banda)
admin.site.register(Albun)