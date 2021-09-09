from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from todoapp.forms import LoginForm,AddForm,AddForm,UpdateForm
from todoapp.models import TodoList
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
@login_required (login_url='/login')
def home(request):
    sdata=TodoList.objects.filter(status='START')
    paginator=Paginator(sdata,5)
    page_number = request.GET.get('page')

    try:
        sdata=paginator.page(page_number)
    except PageNotAnInteger:
        sdata=paginator.page(1)
    except EmptyPage:
        sdata=paginator.page(paginator.num_pages)
    return render(request,'todoapp/home.html',{'sdata':sdata})
from django.contrib.auth import authenticate,logout,login

def loginview(request):
    lform=LoginForm()
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/home')
            else:
                return redirect('/login')

    lform=LoginForm()
    return render(request,'todoapp/login.html',{'lform':lform})
@login_required(login_url='/login')
def listview(request):
    form=AddForm()
    tdata=TodoList.objects.all()
    ddata=TodoList.objects.filter(status='DONE')
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
            return render(request,'todoapp/listview.html',{'form':form,'tdata':tdata,'ddata':ddata})

    return render(request,'todoapp/listview.html',{'form':form,'tdata':tdata,'ddata':ddata})

# update view for details
@login_required(login_url='/login')
def delete_view(request, id):
    ddata=TodoList.objects.get(id=id)
    ddata.delete()
    return redirect('/list')
@login_required(login_url='/login')
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
    logout(request)
    return render(request,'todoapp/logout.html')
