from django.db import models
from cloudinary.models import CloudinaryField

# 
# Create your models here.

class Booster(models.Model):
    BOOSTER_STATUS = (
        ('WA','Awaiting assignment'),
        ('WL','Awaiting launch'),
        ('Rf','Refurbished'),
        ('T','Testing'),
        ('D','Destroyed'),
        ('L','Lost'),
        ('Rt','Retired'),
    )
    number = models.CharField(max_length=16)
    current_status = models.CharField(max_length = 2, choices=BOOSTER_STATUS) 

    def __str__(self):
        return self.number

    def clean(self):
        print('running the "clean() method of Booster!!!')

class LaunchSite(models.Model):
    name = models.CharField(max_length = 64)
    city = models.CharField(max_length = 64)
    state = models.CharField(max_length = 64)
    

    def __str__(self):
        return self.name

class LaunchComplex(models.Model):
    name = models.CharField(max_length = 64)
    launch_site = models.ForeignKey(LaunchSite, on_delete=models.Case)
    image = CloudinaryField('image', null = True, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Launch complexes"
    
class Mission(models.Model):
    name = models.CharField(max_length = 256)
    operator = models.CharField(max_length = 256)
    wikiLink = models.URLField(null = True)
    # image = CloudinaryField('image', null = True)

    def __str__(self):
        return self.name

    def flight_number(self):
        return self.flight.number

class Flight(models.Model):
    OUTCOMES = (
        ('F', 'Failure'),
        ('S', 'Success'),
        ('C', 'Cancelled'),
    )

    number = models.IntegerField()
    date = models.DateField('date of flight')
    booster = models.ForeignKey(Booster, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=1, choices=OUTCOMES)
    launch_complex = models.ForeignKey(LaunchComplex, on_delete=models.CASCADE)
    mission = models.OneToOneField(Mission, on_delete=models.CASCADE)

    def __str__(self):
        return f'No:{self.number} - Booster: {self.booster.number  }' 
