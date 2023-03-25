from django.shortcuts import render
from .models import *
def home(request):
    return render(request,'home.html')
def save(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        mnum=request.POST['mnum']
        pwd=request.POST['pwd']
        if User.objects.filter(email=email).exists():
            data={'message':'email already exist try with new one'}
            return render(request,'home.html',data)
        else:
            user=User.objects.create(fname=fname,lname=lname,email=email,uname=uname,mnum=mnum,pwd=pwd)
            user.save()
            return render(request,'login.html')
    else:
        return render(request,'home.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        if User.objects.filter(email=email).exists():
            if User.objects.filter(pwd=pwd).exists():
                data=User.objects.all()
                return render(request,'show.html',{'data':data})
            else:
                data={'message':'wrong password'}
                return render(request,'login.html',data)
        else:
            data={'message':'wrong email'}
            return render(request,'login.html',data)
    else:
        pass
def log(request):
    return render(request,'login.html')
def delete(request,id):
    id=User.objects.get(id=id)
    id.delete()
    data=User.objects.all()
    return render(request,'show.html',{'data':data})
def logout(request):
    auth.logout(request)
    data={
        'message':'logout successfully'
    }
    return render(request,'login.html',data)
def update(request,id=id):
    data=User.objects.filter(id=id)
    return render(request,'update.html',{'data':data})
def uupdate(request,id=id):

    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    pwd=request.POST['pwd']
    mnum=request.POST['mnum']
    u=User(id=id,fname=fname,lname=lname,mnum=mnum,email=email,pwd=pwd,)
    u.save()
    data=User.objects.all()
    return render(request,'show.html',{'data':data})

 
    