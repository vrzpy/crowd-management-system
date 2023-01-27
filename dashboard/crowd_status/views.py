from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from crowd_status.models import *

# Create your views here.
def StationStatus(request):
    if request.method == 'GET':
        StationDensityList = StationDensity.objects.all().values()

        TowardsADITrainDensity = TrainDensity.objects.filter(TowardsStation__id = 1).values()
        TowardsVAPITrainDensity = TrainDensity.objects.filter(TowardsStation__id = 5).values()


        print(StationDensityList)
        print(TowardsADITrainDensity)
        print(TowardsVAPITrainDensity)

        return JsonResponse({'Station_Status':list(StationDensityList),'Towards_ADI_Status':list(TowardsADITrainDensity), 'Towards_VAPI_Status':list(TowardsVAPITrainDensity)})

    return HttpResponse('Station Status')

def UpdateNews(request):
    if request.method == 'GET':
        AllNews = NewsFeed.objects.all().values()

        return JsonResponse({'News':list(AllNews)})
    
    return HttpResponse('Update News')