from django.urls import path

from . import views

app_name = 'calculators'

urlpatterns = [
    path('sample/', views.sample, name='sample'),
    path('z_criteria/', views.z_criteria, name='z_criteria'),
    path('nps/', views.nps, name='nps'),
]