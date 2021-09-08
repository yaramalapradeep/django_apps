from django.shortcuts import render,redirect
from django.http import HttpResponse
from todoapp.forms import LoginForm,AddForm,AddForm,UpdateForm
from todoapp.models import TodoList
# Create your views here.
def home(request):
    sdata=TodoList.objects.filter(status='START')
    return render(request,'todoapp/home.html',{'sdata':sdata})

def loginview(request):
    lform=LoginForm()
    return render(request,'todoapp/login.html',{'lform':lform})

def listview(request):
    form=AddForm()
    tdata=TodoList.objects.all()
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            title=request.POST['title']
            details=request.POST['details']
            status=request.POST['status']
            rdata=TodoList(
            title=title,
            details=details,
            status=status
            )
            rdata.save()
            form=AddForm()
            return render(request,'todoapp/listview.html',{'form':form,'tdata':tdata})

    return render(request,'todoapp/listview.html',{'form':form,'tdata':tdata})

# update view for details
def delete_view(request, id):
    ddata=TodoList.objects.get(id=id)
    ddata.delete()
    return redirect('/list')

def update_view(request,id):
    uform=UpdateForm()
    if request.method=='POST':
        uform=UpdateForm(request.POST)
        if uform.is_valid():
            nstatus=request.POST['status']
            udata=TodoList.objects.get(id=id)
            udata.status=nstatus
            udata.save()
            return redirect('/list')
    return render(request,'todoapp/update.html',{'uform':uform})

def logoutview(request):
    return render(request,'todoapp/logout.html')
