from django.contrib import admin
from django.urls import path, include
# Importamos desde las views las funciones para cargar nuestras páginas
from .views import index, gatos, perros, cachulo, flaca, ginger, lucifer, nina, thommy

urlpatterns = [
    #Agregamos nuestras páginas
    path('',index,name='INDEX'),
    path('gatos/',gatos,name='GATOS'),
    path('perros/',perros,name='PERROS'),
    path('cachulo/',cachulo,name='CACHULO'),
    path('flaca/',flaca,name='FLACA'),
    path('ginger/',ginger,name='GINGER'),
    path('lucifer/',lucifer,name='LUCIFER'),
    path('nina/',nina,name='NINA'),
    path('thommy/',thommy,name='THOMMY'),
]