from django.contrib import admin
from .models import Booster, Flight,LaunchComplex, LaunchSite , Mission 
# Register your models here.

class LaunchComplexAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'launch_site']


admin.site.register(Booster)
admin.site.register(Flight)
admin.site.register(LaunchComplex, LaunchComplexAdmin)
admin.site.register(LaunchSite)
admin.site.register(Mission)