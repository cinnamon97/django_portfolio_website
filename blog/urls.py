from django.urls import path
from . import views
from django.urls import path, include  # new

urlpatterns= [
    path('myblog',views.myblog,name='myblog')
]

