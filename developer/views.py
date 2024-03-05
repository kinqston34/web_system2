from django.shortcuts import render,redirect


# Create your views here.

def developer(request):
    return render(request,"developer/developer.html")

def login(request):
    return render(request,"developer/login.html")

def logout(request):
    return redirect("developer:login")