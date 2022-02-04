from django.shortcuts import render
# SSR : Server Side Rendering
# CSR : Client Side Rendering
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1><a href='/hello01/test/'>Hello, Django</a></h1>")

def test(request):
    return HttpResponse('<h1><a href="/hello01/">return</a></h1>')

def name(request):
    return HttpResponse('<h1>김채원</h1>')