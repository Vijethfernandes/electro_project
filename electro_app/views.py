from django.shortcuts import render, redirect
from electro_app.forms import reg_form,booking_form,review_form,sub_form
from electro_app.models import customer_request,review
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def index(request):
    name=review_form()
    sub=sub_form()
    data=review.objects.all()
    return render(request, 'index.html',{'rev':name,'revs':data,'key':sub})

def bookings(request):
    name=booking_form(request.POST)
    if name.is_valid():
        data=name.save(commit=False)
        data.connect=request.user
        data.save()
    return render(request, 'bookings.html',{'form':name})

def appointment(request):
    if request.user.is_authenticated:
        name=customer_request.objects.filter(connect=request.user)
        return render(request, 'appointment.html',{'form':name})
    else:
        return render(request,'appointment.html')

def logins(request):
    if request.method=="POST":
        username=request.POST['names']
        password=request.POST['pass']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        return render(request,"logins.html")
    
    return render(request, 'logins.html')

def regs(request):
    name=reg_form(request.POST)
    if name.is_valid():
        name.save()
        return redirect('/logins')
    return render(request,"reg.html",{'form':name})

   

def show(request, ID):
        name=customer_request.objects.get(pk=ID)
        form=booking_form(request.POST or None,instance=name)
        if form.is_valid():
            form.save()
            return redirect('/appointment')
        return render(request, 'show.html',{'show':name})

def delete_items(request, ID):
    data=customer_request.objects.get(pk=ID)
    data.delete()
    return redirect('/appointment')

def logoutuser(request):
    logout(request)
    return redirect('/logins')

def reviews(request):
    name=review_form(request.POST)
    if name.is_valid():
       data = name.save(commit=False)
       data.boss=request.user
       data.save()
    return redirect('/')
    
def delete_reviews(request, ID):
    data=review.objects.get(pk=ID)
    data.delete()
    return redirect('/')

def subscrib(request):
    name=sub_form(request.POST)
    if name.is_valid():
        name.save()
    return redirect('/')