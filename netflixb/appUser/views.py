from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserChild
from django.contrib.auth.models import User

# Create your views here.

# USER
def userLogin(request):
    kullanici = request.user
    print(kullanici)
    if request.method == 'POST':
        # login
      
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('browse')
        else:
            return render(request, 'users/login.html', {
                'hata':'Yanlış kullanıcı adı veya şifre!'
            })
        # register
            
                
    return render(request,'users/login.html')


def userRegister(request):
    if request.method == 'POST':
        name = request.POST['name']
        username1 = request.POST['username1']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            register = User.objects.create_user(
                username=username1, password=password1, first_name=name)
            register.save()
            return redirect('userLogin')
        
    return render(request, 'users/register.html')

def userSettings(request, id):
    profil = UserChild.objects.get(id=id)

    if request.method=='POST':
        new_password1 = request.POST['password1']
        new_password2 = request.POST['password2']
        
        if new_password1 == new_password2:
            user = User.objects.get(id=request.user.id)
            user.set_password(new_password2)
            user.save()
            return redirect('index')
    
    context = {
        'profil':profil
    }
    return render(request, 'users/hesap.html',context)



# PROFIL
def browser(request):
    prof = UserChild.objects.all()
    if request.method=="POST":
        
        name = request.POST["name"]
        files = request.FILES['file']

        if name:    
            profile = UserChild(profilname=name, image=files, user=request.user)
            profile.save()
            
            return redirect('browse')
    
    context = {
        "prof":prof,
    }
    return render(request,'users/browse.html',context)


