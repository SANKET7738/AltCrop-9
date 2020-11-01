from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('input/',views.input, name='input'),
    path('data_upload/',views.data_upload, name='data_upload'),
    path('output/',views.output, name='output'),
    path('contact/',views.contact, name='contact')
]