from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from.models import Booking,Clinics,Outpatient_schedule


def BookingOnline(request):
    all_clinics=Clinics.objects.all()
    if request.method=='POST':
        clinic_id = request.POST['clinic']
        # clinic=request.POST['clinic']
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        clinic = Clinics.objects.get(pk=clinic_id)
        submit=Booking(
            clinics=clinic,
            username=name,
            phonenumber=phone,
            email=email,
            description=message,
        )
        submit.save()
        messages.success(request, 'Information send successfully')
        return redirect('/')
    context={'all_clinics':all_clinics}
    return render(request,'booking/regiter.html',context)



def outpatient_schedule(request):
    schedule=Outpatient_schedule.objects.all()
    context={'schedule':schedule}
    
    return render(request,'booking/table.html',context)