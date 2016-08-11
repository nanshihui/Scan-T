#!/usr/bin/python
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
def hello(request):
    return HttpResponse("Hello world")
def indexpage(request):
    now = datetime.datetime.now()

    return render_to_response('index.html', {'current_date': now})
def test(request):
    return render_to_response('test.html')