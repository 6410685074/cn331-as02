from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Student
from courses.models import Regis,Course
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else :
            messages.success(request,("error wrong password or student id"))
            return redirect('/login')
    else:
        return render(request,'userlogin.html')

def user_logout(request):
    logout(request)
    messages.success(request,("you were logout"))
    return redirect('/login')

def regis(request):
    all_course=Course.objects.all()
    return render(request,'regis.html',{"all_course":all_course})

def account_reg(request):
    user=request.user
    account=Regis.objects.filter(stu_id=user)
    student=Student.objects.get(stu_id=user)
    value_c_id=account.values_list('c_id',flat=True)
    v_cid=[i for i in value_c_id]
    st_id=[j for j in account.values_list('stu_id',flat=True)]
    v_cid=set(v_cid)
    c=Course.objects.all()
    courses=[Course.objects.get(ID=k) for k in v_cid]
    regis=Regis.objects.all()
    a_c=[]
    submit_reg=request.POST.get("c_id")
    cancel=request.POST.get("cancel")
    
    if(len(st_id)==0):
        for c_ in c:
            if c_.nItems<c_.num and c_.status==1:
                    a_c.append(c_)
    elif(len(st_id)>=0):
         a_c=[]
         for c_ in c:
            if c_.nItems<c_.num and c_.status==1 and str(c_.ID) not in value_c_id:
                    a_c.append(c_)
    if(cancel is not None):
        c=Course.objects.get(ID=cancel)
        c.nItems-=1
        c.status=1
        c.save()
        reg=Regis.objects.get(stu_id=user,c_id=cancel)
        reg.delete()
        return redirect('/account_reg')
    
    if(submit_reg is not None):
        ans=Course.objects.get(ID=submit_reg)
        ans.nItems+=1
        if(ans.nItems==ans.num):
            ans.status=0
        ans.save()
        reg=Regis(stu_id=user,c_id=ans)
        reg.save()
        return redirect('/account_reg')
    return render(request,'account_reg.html',{'courses':courses,'a_c':a_c,'user':user,'student':student})
