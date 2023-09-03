from django.contrib import admin
from django.urls import path, include

# Incluindo as url's do app no projeto.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('police_app.urls')),
]
