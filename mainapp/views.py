from django.shortcuts import render,HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("test")

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
