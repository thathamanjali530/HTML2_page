from django.shortcuts import render

# Create your views here.
def firstapp3(request):
    return render(request,'firstapp3.html')
def secondapp3(request):
    return render(request,'secondapp3.html')
from django.http import HttpResponse
def thirdapp3(request):
    return HttpResponse('<center><h1>This is third project,,!!!String as a Response</h1></center>')
    