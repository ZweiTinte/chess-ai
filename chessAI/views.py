from django.shortcuts import render, redirect

from app.log import logLearningProgress
from main import runAILearning

# Create your views here.
def dashboard(request):
    data = logLearningProgress()
    context = {"data": data}
    return render(request, 'chessAI/dashboard.html', context)

def game(request):
    return render(request, 'chessAI/game.html')

def runAI(request):
    runAILearning(int(request.POST['runs']), int(request.POST['turnLimit']))
    return redirect('chess-ai:dashboard')