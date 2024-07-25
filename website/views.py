from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import record

# Create your views here.

def home(request):
    records = record.objects.all()
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate
        user = authenticate(request , username=username , password=password)
        if user is not None:
            # If authentication is successful, log the user in
            login(request,user)
            messages.success(request,"You have been Logged In")
            return redirect('home')
        else:
            # If authentication fails, display an error message
            messages.error(request,'There was something wrong in Logging In, Please try again...')
            return redirect('home')
    else:
        # If the request method is not POST, render the home page
        return render(request,'home.html',{'records':records})


def logout_u(request):
    logout(request)
    messages.success(request,'You have been Logged out Succesfully...')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You have Successfully Registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.error(request,'You must be Logged in to view the records page')
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_record = record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request,'You have deleted the record')
        return redirect('home')
    else:
        messages.error(request,'You must be Logged in to view the records page')
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record Added")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})  
    else:
        messages.error(request,'You must be Logged in to add a Record')
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        customer_record = record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=customer_record)  
        if form.is_valid():
            form.save()
            messages.success(request,'You have updated the record')
            return redirect('home')
        return render(request,'update_record.html',{'form':form}) 
    else:
        messages.error(request,'You must be Logged in to update a Record')
        return redirect('home')
