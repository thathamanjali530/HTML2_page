from django.shortcuts import render

# Create your views here.
def firstapp2(request):
    return render(request,'firstapp2.html')
def secondapp2(request):
    return render(request,'secondapp2.html')

from django.http import HttpResponse
def thirdapp2(request):
    return HttpResponse('<center><h1>This is Third project in app2,,,!!String as a Response</h1></center>')