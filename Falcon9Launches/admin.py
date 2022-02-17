from django.contrib import admin
from .models import Booster, Flight,LaunchComplex, LaunchSite , Mission 
# Register your models here.

class LaunchComplexAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'launch_site']

class MissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','flight_number']


class FlightAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(f'.....admin.py/FlightAdmin/ db_field:{db_field}')
        if db_field.name == "mission":
            kwargs["queryset"] = Mission.objects.filter(flight__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Booster)
admin.site.register(Flight, FlightAdmin)
admin.site.register(LaunchComplex, LaunchComplexAdmin)
admin.site.register(LaunchSite)
admin.site.register(Mission, MissionAdmin)