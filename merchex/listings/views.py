from django.shortcuts import render
from django.http import HttpResponse

def hello(requrst):
    return HttpResponse('<h1>Hello Django</h1>')