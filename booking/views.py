from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from.models import Booking,Clinics


def BookingOnline(request):
    all_clinics=Clinics.objects.all()
    if request.method=='POST':
        clinic=request.POST['clinic']
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        submit=Booking(
            clinics=clinic,
            username=name,
            phonenumber=phone,
            email=email,
            description=message,
        )
        submit.save()
        messages.success(request, 'Information send successfully')
        # return redirect('/')
    context={'all_clinics':all_clinics}
    return render(request,'booking/regiter.html',context)