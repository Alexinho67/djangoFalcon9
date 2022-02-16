from http.client import HTTPResponse
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Booster, LaunchComplex, Mission, Photo, Flight
from django.forms import widgets, ModelForm, ValidationError as myValidationError
from django.views.generic import CreateView, DeleteView, FormView,  UpdateView

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

## MISSIONS ## 

def missions(req):
    
    formMission = MissionCreateForm()
    if req.method == 'POST':
        print(f'@views.missions--> received POST request for new mission: POST:{req.POST}')
        formMission = MissionCreateForm(req.POST)
        if formMission.is_valid():
            print(f'...valid.Saving mission {formMission.instance}')
            formMission.save()
            formMission = MissionCreateForm()
        else:
            print(f'...not valid. Rendering if ValidationError')
    context = {'missions': Mission.objects.all(),
        'secret_message':'Django rules',
        'form': formMission}
    return render(req, 'Falcon9Launches/missions.html', context)

class MissionCreateForm(ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'

    def clean_name(self,*args, **kwargs):
        print('calling "clean_name" method of "MissionCreateForm"')
        name = self.cleaned_data.get('name')
        if (len(name)<=3):
            raise myValidationError('Name is too short!')
        # name += 'ALEX'
        return name    
    
    def clean_operator(self,*args, **kwargs):
        print('calling "clean_operator" method of "MissionCreateForm"')
        operator = self.cleaned_data.get('operator')
        if (len(operator)<=3):
            raise myValidationError('Operator is too short!')
        # name += 'ALEX'
        return operator

def flights(req):

    if(req.method=='POST'):
        print(f'@views.flights--> received POST request for new flight: POST:{req.POST}')
        form = FlightCreateForm(req.POST)
        if form.is_valid():
            print(f'...valid.Saving flight {form.instance}')
            form.save()

        else: 
            print(f'... data NOT valid')
    else:
        # form = FlightCreateForm(initial={'number':999,'date':'aaa','booster': '42' })
        pass
    
    form = FlightCreateForm()
    form.fields['mission'].queryset = Mission.objects.filter(flight__isnull=True)

    flights = Flight.objects.all()
    context = {"flights" : flights,  'form': form}
    return render(req, 'Falcon9Launches/flights.html', context)

class FlightCreateForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }


    


def photos(req):
    print('index.view')
    context = {'photos' : Photo.objects.all()}
    return render(req, 'Falcon9Launches/photos.html', context)

