from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the nmaptool index.")
def indexpage(request):
    now = datetime.datetime.now()

    return render_to_response('index.html', {'current_date': now})