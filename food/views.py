from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import FoodEnergy,Food
@login_required(login_url='login')
def home(request):
    foodlist=Food.objects.all()
    return render(request,'food/food-list.html',context={"foodlist":foodlist})

@login_required(login_url='login')
def test(request):
    return render(request,'food/test.html')
