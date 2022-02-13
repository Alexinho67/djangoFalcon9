from http.client import HTTPResponse
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Booster, LaunchComplex

# Create your views here.

def index(req):
    context ={}
    return render(req,'Falcon9Launches/index.html',context)

def boosters(req):
    if req.method == 'POST':
        boosterNew = Booster(number=req.POST['number'], current_status=req.POST['status'])
        try:
            boosterNew.full_clean()
        except ValidationError as e:
            print('Validation error')
            for m in e.messages:
                print(f'\t message: {m}')
            context = {"boosters" : Booster.objects.all(),
                        "status_choices": Booster.BOOSTER_STATUS,
                        'errorsDict': e.message_dict}
            return render(req, 'Falcon9Launches/boosters.html', context) 
        else:
            boosterNew.save()
            return redirect(reverse('boosters'))

    else: # handle the GET request
        bstrs = Booster.objects.all()
        for b in bstrs:
            print(f'     number: {b.number}')
        print(f'found {len(bstrs)} boosters')
        context = {"boosters" : Booster.objects.all(),
            "status_choices": Booster.BOOSTER_STATUS,
            'errorsDict': None}
    return render(req, 'Falcon9Launches/boosters.html', context)

# def boosterCreate(req):
#     if req.method == 'POST':
#         boosterNew = Booster(number=req.POST['number'], current_status=req.POST['status'])
#         try:
#             boosterNew.full_clean()
#         except ValidationError as e:
#             print('Validation error')
#             for m in e.messages:
#                 print(f'\t message: {m}')
#             context = {"boosters" : Booster.objects.all(),
#                         "status_choices": Booster.BOOSTER_STATUS,
#                         'errorsDict': e.message_dict}
#             return render(req, 'Falcon9Launches/boosters.html', context) 
#         else:
#             boosterNew.save()
#     else:
#         print('no POST method detected')
        
#     return redirect(reverse('boosters'))
#     # context = {"boosters" : Booster.objects.all(),
#     #     "status_choices": Booster.BOOSTER_STATUS}
#     # return render(req, 'Falcon9Launches/boosters.html', context)


def boosterDelete(req, id_booster):
    print(f'boosterDelete')
    if req.method == 'DELETE':
        print(f'deleting booster #{id_booster}')
        booster = get_object_or_404(Booster, pk = id_booster)
        booster.delete()
        # return redirect(reverse('boosters'))
        pathForRedirect = reverse('boosters')
        # print(f'Redirecting user to path: "{pathForRedirect}"')
        return JsonResponse({'success': 'true'})
        
## LAUNCH COMPLEXES 


def launchcomplexes(req):
    complexes = LaunchComplex.objects.all()
    context = {"complexes" : complexes}
    return render(req, 'Falcon9Launches/launchcomplexes.html', context)