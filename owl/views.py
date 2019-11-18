from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def create_sos(request):
    if request.method == "POST":
        form = sosform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_sos')
    else:
        form = sosform()
    return render(request,'owl/home.html',{'form':form})



def home(request):

    return render(request,'home.html')        