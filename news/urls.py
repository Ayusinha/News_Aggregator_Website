from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('sports/', views.sports, name='sports'),
    path('about/', views.about, name='about'),
    path('business/', views.business, name='business'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('general/', views.general, name='general'),
    path('global/', views.globoal, name='globoal'),
    path('health/', views.health, name='health'),
    path('science/', views.science, name='science'),
    path('technology/', views.technology, name='technology'),
]