# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<br>hello world!</br><a href='/blog/about'> About </a>" )

def about(request):
    return HttpResponse("<a href='/blog/'> Index </a>")

