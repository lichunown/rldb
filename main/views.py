from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('''
        debugging...<br>
        <br>Oauth in github can be use:<br>
        please visit:  <a href="/oauth/github/">http://182.254.132.38/oauth/github/</a>
        <br><br><br><br>
        (FUCK Tencent's Oauth.)   
        ''')