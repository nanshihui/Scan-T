#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.views import generic
# Create your views here.
def indexpage(request):
    return HttpResponse("Hello, world. You're at the nmaptool index.")
def login(request):
    if request.method=='GET':
        return render_to_response('nmaptoolview/login.html', {'data':''})
    else:
        if request.POST.get('username','')=='123' and  request.POST.get('password','')=='123':
        
            return render_to_response('nmaptoolview/login.html', {'data':'用户名和密码成功'})  
        return render_to_response('nmaptoolview/login.html', {'data':'登陆错误'})  
def loginvalid(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

