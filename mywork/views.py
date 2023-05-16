from django.shortcuts import render

# Create your views here.

def designes(request):
    return render(request,'mywork/designes.html')

def models(request):
    return render(request,'mywork/models.html')