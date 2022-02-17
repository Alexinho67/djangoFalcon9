from django.core.exceptions import ValidationError
from django.http import  JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Booster, LaunchComplex, LaunchSite, Mission, Photo, Flight
from .forms import BoosterForm, FlightCreateForm, MissionCreateForm

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


def boosterDetails(req, booster_id):
    print(f'@views.boosterDetails. Booster_id:{booster_id}')
    booster = get_object_or_404(Booster, pk = booster_id)
    context ={ 'booster': booster}
    return render(req, 'Falcon9Launches/boosterDetails.html' , context)
    
def boosterEdit(req, booster_id):
    print(f'@views.boosterEdit. Booster_id:{booster_id}')
    booster = get_object_or_404(Booster, pk = booster_id)
    if (req.method == 'POST') :
        form = BoosterForm(req.POST, instance=booster)
        if form.is_valid():
            form.save()
            path = reverse('boosterDetails',args=[booster_id])
            print(f'@EditBooster/POST: redirect to: {path}')
            return redirect(path)
            # return render(req, 'Falcon9Launches/boosterDetails.html' , context)

    form = BoosterForm(instance= booster)
    context ={ 'booster': booster, 'form' : form}
    return render(req, 'Falcon9Launches/boosterEdit.html' , context)

def boosterDelete(req, booster_id):
    booster = get_object_or_404(Booster, pk = booster_id)
    context = {"booster": booster}
    if ((req.method == 'POST') and (req.POST['confirm'] == 'yes')):
        print(f'@views.boosterDelete: Delete booster #{booster_id}')
        booster.delete()
        return redirect(reverse('boosters'))
    else:
        return render(req, 'Falcon9Launches/boosterDelete.html', context)

## LAUNCH COMPLEXES 

def launchcomplexes(req):
    complexes = LaunchComplex.objects.all()
    context = {"complexes" : complexes}
    return render(req, 'Falcon9Launches/launchcomplexes.html', context)
    
def complexDetails(req, complex_id):
    print(f'@views.complexDetails. Complex_id:{complex_id}')
    complex = get_object_or_404(LaunchComplex, pk = complex_id)
    context ={ 'complex': complex}
    return render(req, 'Falcon9Launches/launchcomplexDetails.html' , context)
    

def launchsites(req):
    sites = LaunchSite.objects.all()
    context = {"sites" : sites}
    return render(req, 'Falcon9Launches/launchsites.html', context)

def launchSiteDetails(req, site_id):
    print(f'@views.launchSiteDetails. Site_id:{site_id}')
    launchSite = get_object_or_404(LaunchSite, pk = site_id)
    context ={ 'launchSite': launchSite}
    return render(req, 'Falcon9Launches/launchSiteDetails.html' , context)
    

    

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

def missionDetails(req, mission_id):
    mission = get_object_or_404(Mission, pk = mission_id)

    context = {"mission": mission}
    return render(req, 'Falcon9Launches/missionDetails.html', context)

def missionEdit(req, mission_id):
    print(f'@views.missionEdit. Mission_id:{mission_id}. Method:{req.method}')
    mission = get_object_or_404(Mission, pk = mission_id)
    if req.method =='POST':
        pass
        form = MissionCreateForm(req.POST, instance=mission)
        if form.is_valid():
            form.save()
            ## return to mission details
            return redirect(reverse('missionDetails',args=[mission.id]))
        else:
            print('....form is not valid.Errors: {form.errors}')
            context ={ 'mission': mission, 'form':form}
            return render(req, 'Falcon9Launches/missionEdit.html' , context)
    form = MissionCreateForm(instance=mission, use_required_attribute=False)
    context ={ 'mission': mission, "form":form }
    return render(req, 'Falcon9Launches/missionEdit.html' , context)

def missionDelete(req, mission_id):
    print(f'@views.missionDelete. mission_id:{mission_id}. Method: {req.method}')
    mission = get_object_or_404(Mission, pk = mission_id)
    if (req.method == 'POST') and (req.POST['confirm'] == 'yes'):
        mission.delete()
        return redirect(reverse('missions'))
    context ={'mission': mission}
    return render(req, 'Falcon9Launches/missionDelete.html' , context)

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
    flights = Flight.objects.all().order_by('date')
    context = {"flights" : flights,  'form': form}
    return render(req, 'Falcon9Launches/flights.html', context)


def flightDetails(req, flight_id):
    print(f'@views.flightDetails. Flight_id:{flight_id}')
    flight = get_object_or_404(Flight, pk = flight_id)
    context ={ 'flight': flight}
    return render(req, 'Falcon9Launches/flightDetails.html' , context)
    
def flightEdit(req, flight_id):
    print(f'@views.flightEdit. Flight_id:{flight_id}. Method:{req.method}')
    flight = get_object_or_404(Flight, pk = flight_id)
    if req.method =='POST':
        form = FlightCreateForm(req.POST, instance=flight)
        if form.is_valid():
            form.save()
            ## return to flight details
            return redirect(reverse('flightDetails',args=[flight.id]))
        else:
            print('....form is not valid.Errors: {form.errors}')
            context ={ 'flight': flight, 'form':form}
            return render(req, 'Falcon9Launches/flightEdit.html' , context)
    form = FlightCreateForm(instance=flight)
    context ={ 'flight': flight, 'form':form}
    return render(req, 'Falcon9Launches/flightEdit.html' , context)

def flightDelete(req, flight_id):
    print(f'@views.flightDelete. Flight_id:{flight_id}. Method: {req.method}')
    flight = get_object_or_404(Flight, pk = flight_id)
    if (req.method == 'POST') and (req.POST['confirm'] == 'yes'):
        flight.delete()
        return redirect(reverse('flights'))
    context ={'flight': flight}
    return render(req, 'Falcon9Launches/flightDelete.html' , context)


    


def photos(req):
    print('index.view')
    context = {'photos' : Photo.objects.all()}
    return render(req, 'Falcon9Launches/photos.html', context)

