from django.contrib import messages, auth
from django.contrib.auth.models import User


from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['user name']
        Password = request.POST['password']
        user =auth.authenticate(username=username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credential')
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username = request.POST['user name']
        FirstName = request.POST['First_name']
        LastName = request.POST['Last_name']
        Email_address = request.POST['Email_address']
        Password = request.POST['Password']
        Cpassword = request.POST['ConfirmPassword']
        if Password==Cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request,"UserName Already Exists")
                return redirect('register')
            elif User.objects.filter(email = Email_address).exists():
                messages.info(request, "Email Already Exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=FirstName,last_name=LastName,email=Email_address,password=Password)

            user.save()
            return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')