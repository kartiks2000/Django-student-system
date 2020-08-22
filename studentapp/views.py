from django.shortcuts import render,redirect

from studentapp.models import stdmodel
from studentapp.forms import addform

# Create your views here.

def home(request):
    return render(request,'home.html',context={})

def add(request):
    if request.method == 'POST':
        f = addform(request.POST)
        if f.is_valid():
            f.save()
            response = redirect('/show')
            return response 
    else: 
        f = addform()       
    return render(request,'add.html',context={'form':f})

def edit(request,myid):
    abc = stdmodel.objects.get(id=myid)
    if request.method == 'POST':
        f = addform(request.POST, instance=abc)
        if f.is_valid():
            f.save()
            response = redirect('/show')
            return response 
    else: 
        f = addform(instance=abc)       
    return render(request,'edit.html',context={'form':f})   

def chooseedit(request):
    alll = stdmodel.objects.all()
    return render(request,'chooseedit.html',context={'myl' : alll})     

def choosenid(request):   
    sid = request.POST['sid'] 
    redir = "/edit/"+sid
    return redirect(redir)

def show(request):
    alll = stdmodel.objects.all()
    return render(request,'show.html',context={'myl' : alll}) 


def delete(request,myid):
    x = stdmodel.objects.get(id=myid)
    x.delete()
    response = redirect('/show')
    return response           
