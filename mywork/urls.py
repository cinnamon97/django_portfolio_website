from django.urls import path
from . import views

urlpatterns= [
    path('designes',views.designes,name='designes'),
    path('models',views.models,name='models')
]