from django.http import HttpResponse
from django.shortcuts import render

from . models import place
from . models import team


# Create your views here.


def travelapp(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,'index.html',{'results':obj,'teammate':obj1})




