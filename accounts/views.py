from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else :
        if request.method == "POST":
            form = RegistrationForm(request.POST or None)
            
            if form.is_valid():
                user = form.save()
                
                row_password = form.cleaned_data.get('password2')
                
                user = authenticate(username = User.username,password = row_password)
                
                login(request,user)
                
                return redirect ("home")
        else :
            form =RegistrationForm()
        return render(request,"register.html",{"form" : form})

# login user

def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    else :
        if request.method == "POST":
            username =  request.POST['username']
            password =  request.POST['password']
            
            user = authenticate(username=username,password=password)
            
            if user is not None :
                if user.is_active:
                    login(request,user)
                    return redirect('home')
                else :
                    return render (request ,"login.html",{"error":"Your account has been disabled"})
            else :
                return render(request,"login.html",{"error":"Invalid username or password"})
        return render(request,"login.html")

# logout user

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")
    else :
        return redirect("login.html")
            