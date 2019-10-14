from django.shortcuts import render
from remaind.models import *
from datetime import date
from django.contrib import messages

# Create your views here.
def viewremainder(request):
    today = date.today()
    remaind=remaindtbl.objects.filter(date=today,loginuser=request.session["id"])
    return render(request,'index.html',context={'con':remaind})
def viewaddevent(request):
    return render(request,'addevents.html')
def addevents(request):
   if(request.method=='POST'):
        obj=remaindtbl()
        obj.name=request.POST.get("name")
        obj.quotes=request.POST.get("quotes")
        obj.date=request.POST.get("date")
        obj.subject=request.POST.get("subject")
        obj.loginuser=request.session["id"]
        obj.save()
        return viewremainder(request)


def editevents(request,id):
    obj=id
    if(request.method=='POST'):

        remaind = remaindtbl.objects.filter(userid__exact=obj)
        return render(request, 'editevents.html', context={'con': remaind})
    if (request.method == 'GET'):

        name=request.GET.get("name")
        quotes=request.GET.get("quotes")
        date=request.GET.get("date")
        subject=request.GET.get("subject")
        remaindtbl.objects.filter(userid=id,loginuser=request.session["id"]).update(name=name,quotes=quotes,date=date,subject=subject)
        return viewremainder(request)
def viewhome(request):
    return render(request, 'home.html')
def viewsignup(request):
         return render(request, 'signup.html')
def signup(request):

    if(request.method=='POST'):
        obj=usertable()
        obj.name=request.POST.get("usernamesignup")

        obj.password=request.POST.get("passwordsignup")
        obj.save()
        return viewhome(request)
def login(request):
    if(request.method=='POST'):
        username=request.POST.get("username")
        password=request.POST.get("password")
        if(usertable.objects.filter(name=username,password=password)).exists():
            getid=usertable.objects.filter(name=username, password=password)
            for i in getid:
                id = i.id
            request.session['id'] =id
            return viewremainder(request)

        else:
            return viewhome(request)


def allevents(request):
    remaind = remaindtbl.objects.filter(loginuser=request.session["id"])
    return render(request, 'allevents.html', context={'con': remaind})
def find(request):

    today = request.POST.get("date")
    remaind=remaindtbl.objects.filter(date=today,loginuser=request.session["id"])
    return render(request,'find.html',context={'con':remaind,'today':today})
def delete(request,id):
    obj=id
    remaindtbl.objects.filter(userid=obj, loginuser=request.session["id"]).delete()
    return allevents(request)