from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def signup(reqest):
    if reqest.method == 'GET':
        signupForm = UserCreationForm()
        return render(reqest,'users/signup.html',
                      {'signupForm': signupForm})
    elif reqest.method == "POST" :
        signupForm = UserCreationForm(reqest.POST)
        if signupForm.is_valid():
            signupForm.save()
            return redirect('/')

def userslogin(request):
    if request.method == "GET" :
        loginForm = AuthenticationForm()
        return render(request,'users/login.html',
                      {'loginForm' : loginForm})


    elif request.method == "POST" :
        loginForm = AuthenticationForm(request,request.POST)
        if loginForm.is_valid():
            login(request, loginForm.get_user())
            return redirect('/')
        else :
            return redirect('users:login')

def userslogout(requset):
    logout(requset)
    return redirect('users:login')