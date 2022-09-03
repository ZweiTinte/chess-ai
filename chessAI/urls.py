from django.urls import path

from . import views

app_name = 'chess-ai'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('ai-run', views.runAI, name="runAI")
]