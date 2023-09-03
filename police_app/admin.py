from django.contrib import admin
from .models import Pessoa, Ocorrencia

# Registrando as tables no /admin

admin.site.register(Pessoa)
admin.site.register(Ocorrencia)