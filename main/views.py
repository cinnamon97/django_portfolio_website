from django.shortcuts import render
from .models import Contact
# Create your views here.

def home(request):
    return render(request,'main/home.html')
#insert into db

def mycontacts(request):
    if request.method=='POST':
        v_name=request.POST.get('name')
        v_email=request.POST.get('email')
        v_subject=request.POST.get('subject')
        v_message=request.POST.get('message')

        v_contact= Contact(name=v_name, email=v_email, subject=v_subject, message=v_message)
        v_contact.save()

        return render(request, 'main/thanks.html')

    else: return render(request,'main/mycontacts.html')


    