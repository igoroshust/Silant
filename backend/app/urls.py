from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('main/', main_view, name='main'),
    path('detail-machine/', detail_machine, name='detail_machine'),
    path('about-machine/', about_machine, name='about_machine'),
]