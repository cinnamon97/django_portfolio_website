from django.urls import path
from . import views

urlpatterns=[
    path('mycontacts',views.mycontacts,name='mycontacts'),
    path('',views.home,name='home')
]