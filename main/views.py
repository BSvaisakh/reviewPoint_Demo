from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from . forms import *

# Create your views here.

def home(request):
    allMovies = Movie.objects.all()  #select * from movies
    context = {
        "movies" : allMovies,
    }
    return render(request,"index.html",context)

# detail page

def detail(request,id):
    movie = Movie.objects.get(id=id) #select * from movie where id = id
    context = {
        "movie" : movie,
    }
    return render(request,"details.html",context)

# Add movies to the database

def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = Movieform(request.POST or None)
                
                # Check if the form is valid
                if form.is_valid():
                    data=form.save(commit=False)
                    data.save()
                    return redirect("home")
            else :
                form =Movieform()
            return render(request,"addmovies.html",{"form": form,"caption":"Add Movies"})
        else :
            return redirect ("home")
    return redirect ("login")

def edit_movies(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie = Movie.objects.get(id=id)
            
            # form check
            if request.method=="POST":
                form = Movieform(request.POST or None,instance=movie)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("detail",id)
            else :
                form = Movieform(instance=movie)
            return render(request,"addmovies.html",{"form":form,"caption":"Edit Movies"})
        else :
            return redirect ("home")
    return redirect ("login")

def delete_movies(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie = Movie.objects.get(id=id)
            movie.delete()
            return redirect("home")
        else :
            return redirect ("home")
    return redirect ("login")
                    
