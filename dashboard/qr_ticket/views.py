from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import *
# Create your views here.

@login_required(login_url='login')
def source(request):
    obj = TicketHistory.objects.filter(
        user = request.user,
        Source = request.GET.get('name'),
        Price = 0
    )

    if len(obj) == 0:
        obj = TicketHistory.objects.create(user = request.user, Source = request.GET.get('name'))
        obj.save()

    return redirect('home_index')

@login_required(login_url='login')
def destination(request):
    obj = TicketHistory.objects.filter(
        user = request.user,
        Price = 0
    )

    if len(obj) == 1:
        obj = TicketHistory.objects.get(
            user = request.user,
            Price = 0
        )

        obj.Destination = request.GET.get('name')
        obj.Price = TicketPricing.objects.get(Source=obj.Source,Destination=request.GET.get('name')).Price
        obj.save()

    return redirect('home_index')