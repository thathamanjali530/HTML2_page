from django.urls import path
from app3.views import *
app_name='project10'
urlpatterns=[
    path('firstapp3/',firstapp3,name='firstapp3'),
    path('secondapp3/',secondapp3,name='secondapp3'),
    path('thirdapp3/',thirdapp3,name='thirdapp3'),
]