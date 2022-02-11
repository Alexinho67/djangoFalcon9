import django
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Booster
# Create your views here.


def index(req):
    context ={}
    return render(req,'Falcon9Launches/index.html',context)

def boosters(req):
    context = {"boosters" : Booster.objects.all(),
        "status_choices": Booster.BOOSTER_STATUS}
    return render(req, 'Falcon9Launches/boosters.html', context)

def boosterCreate(req):
    if req.method == 'POST':
        boosterNew = Booster(number=req.POST['number'], current_status=req.POST['status'])
        boosterNew.save()
    else:
        print('no POST method detected')
        
    return redirect(reverse('boosters'))
    # context = {"boosters" : Booster.objects.all(),
    #     "status_choices": Booster.BOOSTER_STATUS}
    # return render(req, 'Falcon9Launches/boosters.html', context)