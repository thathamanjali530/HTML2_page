from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('firstapp1/',firstapp1,name='firstapp1'),
    path('secondapp1/',secondapp1,name='secondapp1'),
    path('thirdapp1/',thirdapp1,name='thirdapp1'),
]