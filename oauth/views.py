from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.http import urlquote
from m_user.models import Muser
from django.http import HttpResponse
from urllib import urlopen
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

def oauth_github(request):
    if request.method=='POST':
        return  HttpResponse(str(request.POST.get('access_token','')))         
    if request.GET.get('code',''):
        code = request.GET.get('code','')
        data = {
            #'grant_type': 'authorization_code',
            'client_id': '9eeff0489380af861366',
            'client_secret': '394455b79fd571b04e241bc208edc720fd2fea57',
            'code': code,
            'redirect_uri': 'http://182.254.132.38/oauth/github',        
            'state':'test',
        }  
        #return HttpResponseRedirect("https://github.com/login/oauth/access_token?"+getGETdata(data))
        webdata = urlopen("https://github.com/login/oauth/access_token?"+getGETdata(data)).read()
        return HttpResponse(str(webdata))
    else:
        data = {
            #'grant_type': 'authorization_code',
            'client_id': '9eeff0489380af861366',
            #'client_secret': '394455b79fd571b04e241bc208edc720fd2fea57',
            #'code': code,
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
