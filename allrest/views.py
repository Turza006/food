from django.shortcuts import render
from .models import Allrest


def home(request):
    allrest = Allrest.objects
    return render(request,'home.html',{'allrest':allrest})








