from django.urls import path
from app2.views import *
app_name='Nothing'
urlpatterns=[
    path('firstapp2/',firstapp2,name='firstapp2'),
    path('secondapp2/',secondapp2,name='secondapp2'),
    path('thirdapp2/',thirdapp2,name='thirdapp2')
]