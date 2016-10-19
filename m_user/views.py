from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from models import Muser
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def userexist(username):
    if User.objects.filter(username=username):
        return True
    else:
        return False

def mlogin(request):
    pass
def mlogup(request):
    pass
def ologin(request,username):
    user = authenticate(username=username, password='admin')
    if user is not None and user.is_active: 
        login(request,user)
        return HttpResponse("login")
def ologup(request,username,password,u_id,name):
    user = User()
    user.username = username
    user.set_password(password)
    user.save()
    muser =Muser()
    muser.user = user
    muser.truename = name
    muser.u_id = u_id
    muser.save()
    return ologin(request,username)