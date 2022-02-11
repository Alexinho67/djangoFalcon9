from django.db import models

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

class LaunchSite(models.Model):
    name = models.CharField(max_length = 64)
    city = models.CharField(max_length = 64)
    state = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class LaunchComplex(models.Model):
    name = models.CharField(max_length = 64)
    launch_site = models.ForeignKey(LaunchSite, on_delete=models.Case)

    def __str__(self):
        return self.name
    
class Mission(models.Model):
    name = models.CharField(max_length = 256)
    operator = models.CharField(max_length = 256)
    
    def __str__(self):
        return self.name

class Flight(models.Model):
    OUTCOMES = (
        ('F', 'Failure'),
        ('S', 'Success'),
        ('C', 'Cancelled'),
    )

    flight_number = models.IntegerField(max_length=16)
    date = models.DateField('date of flight')
    booster = models.ForeignKey(Booster, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=1, choices=OUTCOMES)
    launch_site = models.ForeignKey(LaunchSite, on_delete=models.CASCADE)
    mission = models.OneToOneField(Mission, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight_number}/{self.booster.name}' 