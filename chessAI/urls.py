from django.urls import path

from . import views

app_name = 'chess-ai'
urlpatterns = [
    path('', views.index, name='index')
]