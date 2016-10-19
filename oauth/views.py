from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.http import urlquote
from m_user.models import Muser
from django.http import HttpResponse
from urllib import urlopen
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re,json
# Create your views here.
GITHUB_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_CLIENTID = '1fa8c369d5e0de863df2'  
GITHUB_CLIENTSECRET = '4dd3020c23cfc0816137e3a0176198212bf0d7f5' 
GITHUB_CALLBACK = 'http://182.254.132.38/oauth/github/get'

def getGETdata(data):
    temp = ""
    for item in data:
        temp += "%s=%s&" % (item,urlquote(data[item]))
    print temp
    return temp
def getaccess_token(data):
    print "data=%s" % data
    pattern = re.compile(r'access_token=(.*?)&')
    match = pattern.match(str(data))
    return str(match.group(1))

def datasave(request,data,platform):
    print data
    if platform=='github':
        mlogin = data['login']#username
        name = data['name']
        u_id = str(data['id'])
        # print 'username:%s' % data['login']
        # print 'name:%s' % data['name']
        # print 'id :%s' % str(data['id'])
        if Muser.objects.filter(u_id=u_id):#account is exist
            user = authenticate(username=mlogin, password='admin')
            login(request,user)
            return ({'result':'exist','username':mlogin,'name':name,},request)
        else:#account is not exist
            user = User(username=mlogin,password='admin')
            user.save()
            muser = Muser(user=user,u_id=u_id,truename=name)
            muser.save()
            user = authenticate(username=mlogin, password='admin')            
            login(request,user)
            return ({'result':'new','username':mlogin,'name':name,},request)

def oauth_github(request):       
    if request.GET.get('code',''):#Then get access_token
        code = request.GET.get('code','')
        data = {
            #'grant_type': 'authorization_code',
            'client_id': '9eeff0489380af861366',
            'client_secret': '394455b79fd571b04e241bc208edc720fd2fea57',
            'code': code,
            'redirect_uri': 'http://182.254.132.38/oauth/github',        
            'state':'test',
        }  
        webdata = urlopen("https://github.com/login/oauth/access_token?"+getGETdata(data)).read()
        userdata = urlopen("https://api.github.com/user?access_token="+getaccess_token(webdata)).read()
        userdata = json.loads(userdata)
        (data,request) = datasave(request,userdata,'github')
        if data['result']=='new':
            return HttpResponse("create new account.")
        elif data['result']=='exist':
            return HttpResponse("have login")
    else:#first :get code
        data = {
            'client_id': '9eeff0489380af861366',
            'redirect_uri': 'http://182.254.132.38/oauth/github',        
            'state':'test',
        }
        return HttpResponseRedirect("https://github.com/login/oauth/authorize?"+getGETdata(data))      
#https://graph.qq.com/oauth2.0/authorize?response_type=token&client_id=1105688899&redirect_uri=http%3A//182.254.132.38/oauth/tencent/get&scope=get_user_info
def oauth_tencent(request):
    data = {
        'response_type':"code",
        'client_id':'1105688899',
        'redirect_uri':'http://182.254.132.38/oauth/tencent/get',
        #'expires_in':'7776000',
        'state':'test',
    }
    return HttpResponseRedirect("https://graph.qq.com/oauth2.0/authorize?"+getGETdata(data))
def oauth_tencent_get(request):
    code = request.GET.get("code",'')
    if code:
        print "code = %s" % code
        data = {
            'grant_type':'authorization_code',
            'client_id':'1105688899',
            'client_secret':'NTwviSAhQpi6EjjV',
            'code':code,
            'redirect_uri':'http://182.254.132.38/oauth/tencent/get',
        }
        return HttpResponseRedirect("https://graph.qq.com/oauth2.0/token?"+getGETdata(data))
    else:
        access_token = request.GET.get("access_token",'')
        expires_in = request.GET.get("expires_in",'')
        refresh_token = request.GET.get("refresh_token",'')
        return HttpResponse(str(access_token))
