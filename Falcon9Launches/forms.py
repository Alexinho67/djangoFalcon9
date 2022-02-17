from django.forms import widgets, ModelForm, ValidationError
from .models import Booster, Mission, Flight
from django.contrib.auth.models import User
class MissionCreateForm(ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'

    def clean_name(self,*args, **kwargs):
        print('calling "clean_name" method of "MissionCreateForm"')
        name = self.cleaned_data.get('name')
        if (len(name)<=3):
            raise ValidationError('Name is too short!')
        # name += 'ALEX'
        return name    
    
    def clean_operator(self,*args, **kwargs):
        print('calling "clean_operator" method of "MissionCreateForm"')
        operator = self.cleaned_data.get('operator')
        if (len(operator)<=3):
            raise ValidationError('Operator is too short!')
        # name += 'ALEX'
        return operator


class FlightCreateForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super (FlightCreateForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['mission'].queryset = Mission.objects.filter(flight__isnull=True)
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }
class BoosterForm(ModelForm):

    class Meta:
        model= Booster
        fields = '__all__'


class MyUserRegistration(ModelForm):

    class Meta:
        model = User
        fields = ['username','password']