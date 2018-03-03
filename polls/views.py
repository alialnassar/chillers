from django.shortcuts import render
from polls.models import Chiller

def index(request):
    try:
        chillers = Chiller.objects.all()
    except Chiller.DoesNotExist:
        chillers = None
        
    context = {
        'chillers':chillers
    }
    
    return render(request, 'polls/index.html', context)

def chiller_detials(request, chiller_id):
    try:
        chiller = Chiller.objects.get(pk=chiller_id)
    except Chiller.DoesNotExist:
        chiller = None
        
    context = {
        'chiller':chiller
    }
    
    return render(request, 'polls/chiller_details.html', context)

def login(request):
    #username = request.POST['username']
    #password = request.POST['password']
    
    return render(request, 'polls/login.html')