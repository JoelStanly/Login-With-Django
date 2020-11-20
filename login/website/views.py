from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginDetails
# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def create(response):
    if response.method == "POST":
        form1=LoginDetails(response.POST)
        if form1.is_valid():
            n=form1.cleaned_data["name"]
            p=form1.cleaned_data["password"]
            return render(response,"base.html",{})
    else:
        form=LoginDetails()
        return render(response,"create.html",{"form":form})