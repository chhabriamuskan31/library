from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    # return HttpResponse("Hello this is register page")
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")
