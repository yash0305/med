from django.http import HttpResponse
from .models import *

from django.shortcuts import render

def index(request):
    data = Med.objects.all()
    context= {'data':data}

    return render(request, 'index.html', context)



def signup(request):
    return render(request, 'signup.html')




def loginPage(request):
    return render(request, 'loginPage.html')

def base(request):
    return render(request, 'base.html')

