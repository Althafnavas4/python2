from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(req):
    return HttpResponse('welcome')
def fun2(req):
    return HttpResponse('new')


