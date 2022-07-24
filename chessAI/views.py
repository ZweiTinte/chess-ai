from django.shortcuts import render

from app.log import logLearningProgress

# Create your views here.
def index(request):
    data = logLearningProgress()
    context = {"data": data}
    return render(request, 'chessAI/index.html', context)