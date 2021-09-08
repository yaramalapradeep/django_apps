from django.shortcuts import render
from todoapp.forms import LoginForm,AddForm,AddForm
# Create your views here.
def home(request):
    return render(request,'todoapp/home.html')

def loginview(request):
    form=LoginForm()
    return render(request,'todoapp/login.html',{'form':form})

def listview(request):
    form=AddForm()
    return render(request,'todoapp/listview.html',{'form':form})

def logoutview(request):
    return render(request,'todoapp/logout.html')
