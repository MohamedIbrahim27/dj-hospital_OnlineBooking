from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from inquiries_complaints.models import inquiries
from.models import settings


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
    informatins=settings.objects.first()
    return render(request,'settings/index.html',
                    {'informatins':informatins})