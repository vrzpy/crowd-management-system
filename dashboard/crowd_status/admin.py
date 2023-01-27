from django.contrib import admin


from .models import *
# Register your models here.
admin.site.register(StationInfo)
admin.site.register(StationDensity)
admin.site.register(TrainDensity)
admin.site.register(NewsFeed)