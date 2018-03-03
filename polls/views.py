from django.shortcuts import render
from polls.models import Chiller
from django.http import HttpResponse

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

def add_chiller(request):
    if request.method == "post":
        status = request.POST['status']
        temp = request.POST['temp']
        
        chiller = Chiller()
        chiller.status = status
        chiller.temprature = temp
        if chiller.save():
            return HttpResponse("chiller has been created successfully")
    
    return render(request, 'polls/add_chiller.html')
