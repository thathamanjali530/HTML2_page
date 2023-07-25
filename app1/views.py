from django.shortcuts import render

# Create your views here.
def firstapp1(request):
    return render(request,'firstapp1.html')
def secondapp1(request):
    return render(request,'secondapp1.html')
    
from django.http import HttpResponse
def thirdapp1(request):
    return HttpResponse('<h1>This is Third project,,,,!String as a Response</h1>')