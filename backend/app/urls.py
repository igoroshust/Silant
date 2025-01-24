from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_view, name='search'),
    path('main/', main, name='main'),
    path('detail-machine/', detail_machine, name='detail_machine'),
    path('about-machine/', about_machine, name='about_machine'),
]