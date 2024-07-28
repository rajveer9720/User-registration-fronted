
from django.contrib.auth.forms import User
from django.contrib import messages
from django.shortcuts import redirect,render

def index(request):
    return render(request,'user/index.html')


def register(request):
    if request.method =='POST':
        fname =request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1  = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username=username, pass1=pass1,email=email,fname=fname,lname=lname)

        myuser.save()

        print("Your account has been succesfully create")
        return redirect('/')
    else:
        return render(request,'user/register.html')
