from django.urls import path

from . import views

app_name = 'chess-ai'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('game', views.game, name='game'),
    path('ai-run', views.runAI, name="runAI")
]