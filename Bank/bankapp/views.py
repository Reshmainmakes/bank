from django.contrib import auth,messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def demo(request ):

    return render (request,"index.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('button')
        else:
            messages.info(request,"invalid credentials")
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        password1 = request.POST['password1']
        if password== password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    print("user created")
    return render(request,'register.html')

def form(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        # dob= request.POST['dob']
        # age= request.POST['age']
        # gender= request.POST['gender']
        # phone_number= request.POST['phone_number']
        email = request.POST['email']
        # address= request.POST['address']
        # district = request.POST['district']
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email exist")

            return redirect('form')
        else:
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email)
            user.save();
            messages.info(request, "Application Accepted")
            return redirect('form')

    return render(request,'form.html')


def button(request ):

    return render(request,"button.html")