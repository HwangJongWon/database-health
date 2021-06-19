from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from foods.models import Fitness
# Create your views here.

def index(request):
    context=dict()
    today=datetime.today().date()
    fitnessen=Fitness.objects.all()
    context={"date":today}
    context["fitnessen"]=fitnessen
    return render(request, 'foods/index.html', context=context)



def health_detail(request, pk):
    context=dict()
    fit=Fitness.objects.get(id=pk)
    context["fit"]=fit
    return render(request, 'foods/detail.html', context=context)