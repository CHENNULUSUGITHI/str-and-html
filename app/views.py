from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def bujji(request):
    return HttpResponse('bujji is one of the mental pilla')

def angel(request):
    return HttpResponse('<marquee><h1>one of the beautiful girl in the world </h1></marquee>')

def amma(request):
    return render(request,'amma.html')

def shilpa(request):
    return render(request,'shilpa.html')