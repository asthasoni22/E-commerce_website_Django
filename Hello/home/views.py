from imaplib import _Authenticator
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def index(request):   
    return render(request , 'index.html')

def login(request):
    if request.method == "POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            data=UserRegister.objects.get(email=email1,password=password1)
            if data:
                request.session['email']=data.email
                print(request.session['email'])
                return redirect('index')
            else:
                return render(request,'login.html',{'message':'Invalid email or password'})
        except:
            return render(request,'login.html',{'message':'Invalid email or password'})
    return render(request,'login.html')

def logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('index')
    else:
        return redirect('index')
from django.core.mail import send_mail

def forgot(request):
    if request.POST:
        useremail=request.POST['email']
        try:
            data=UserRegister.objects.get(email=useremail)
            if data:
                send_mail(
                "Forgot Password",
                "Dear " +str(data.name)+"\n Your Password is :"+str(data.password),
                "youremail",
                [useremail],
                fail_silently=False,
                )
                return render(request,'forgot.html',{'message':'Password  Sent To Your Email'})
            else:
                return render(request,'forgot.html',{'message':'Email Id Not Found'})
        except:
            return render(request,'forgot.html',{'message':'Email Id Not Found'})
    return render(request,'forgot.html')




def table_all(request):
    a=UserRegister.objects.all()
    print("data",a)
    return render(request,'table.html',{"data":a})


def table_filter(request):
    a=UserRegister.objects.filter(email='demo@gmail.com')
    print("data",a)
    return render(request,'table.html',{"data":a})


def table_get(request):
    a=UserRegister.objects.get(email='d@gmail.com')
    print("data",a)
    return render(request,'table_get.html',{"data":a})

def index(request):
    if 'email' in request.session:
        a=request.session['email']
        data=Category.objects.all()
        return render(request,'base.html',{'data':data,'a':a})
    else:
        data=Category.objects.all()
        return render(request,'index.html')#,{'data':data}

# def productall(request):
#     if 'email' in request.session:
#         a=request.session['email']
#         data=Product.objects.all()
#         return render(request,'productall.html',{'data':data,'a':a})
#     else:
#         data=Product.objects.all()
#         return render(request,'productall.html',{'data':data})

# def productcategorywise(request,id):
#     if 'email' in request.session:
#         a=request.session['email']
#         data=Product.objects.filter(category=id)
#         return render(request,'productall.html',{'data':data,'a':a})
#     else:
#         data=Product.objects.filter(category=id)
#         return render(request,'productall.html',{'data':data})  


# def singleproduct(request,id):
#     if 'email' in request.session:
#         a=request.session['email']
#         data=Product.objects.get(pk=id)
#         return render(request,'singleproduct.html',{'data':data,'a':a})
#     else:
#         data=Product.objects.get(pk=id)
#         return render(request,'singleproduct.html',{'data':data})
    
def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        password1=request.POST['password']
        # phone1=request.POST['phone']
        # address1=request.POST['address']
        # print(name1,email1,password1)
        data=UserRegister(name=name1,email=email1,password=password1)
        a=UserRegister.objects.filter(email=email1)
        data.save()
        messages.success(request, "please login")
        
        # if len(a)==0:
        #     data.save()
        #     return redirect('login')
        # else:
        #     return render(request,'register.html',{'message':"user alredy exist"}) 

    return render(request,'register.html')  

def changepass(request):
    if 'email' in request.session:
        a=request.session['email']
        user=UserRegister.objects.get(email=a)
        if request.method=="POST":
            old=request.POST['oldpass']
            newpass=request.POST['newpass']
            newpass1=request.POST['newpass1']
            if old==user.password:
                if newpass==newpass1:
                    user.password=newpass
                    user.save()
                    return render(request,'changepass.html',{'message':"New password update",'a':a})
                else:
                    return render(request,'changepass.html',{'message':"New password not match",'a':a})
            else:
                return render(request,'changepass.html',{'message':"Old password not match",'a':a})
            
        return render(request,'changepass.html',{'a':a})
    else:
        return redirect('login1')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request, "Your message has been sent")
    return render(request , 'contact.html')

def bottoms(request):
    return render(request, 'bottoms.html')

def tops(request):
    return render(request, 'tops.html')

def jwellery(request):
    return render(request, 'jwellery.html')

def traditionals(request):
    return render(request, 'traditionals.html')

def products(request):
    return render(request, 'products.html')

def additional(request):
    return render(request, 'additional.html')

def register(request):
    return render(request, 'register.html')

def forgot(request):
    return render(request,'forgot.html')