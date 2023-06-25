from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from inquiries_complaints.models import inquiries


def home(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        message=request.POST['message']
        submit=inquiries(
            username=name,
            phonenumber=phone,
            message=message,
        )
        submit.save()
        messages.success(request, 'Information send successfully')
        return redirect('/')
    return render(request,'settings/index.html')