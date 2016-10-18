from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.http import urlquote
from m_user.models import Muser
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
    content = {
        'grant_type': 'authorization_code',
        'client_id': GITHUB_CLIENTID,
        'client_secret': GITHUB_CLIENTSECRET,
        'code': code,
        'redirect_uri': GITHUB_CALLBACK,        
    }
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
