from email import contentmanager
from http.client import HTTP_VERSION_NOT_SUPPORTED, ImproperConnectionState
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import date, datetime

# 데이터를 꺼내와 화면에 나타내고 싶은 것들의 로직
def index(request):
    now = datetime.now()
    context = {
        'current_date' : now
    }    
    return render(request, 'first/index.html', context)


def select(request):
    context={'number' : 4}
    return render(request, 'first/select.html', context)


def result(request):
    context={'numbers' : [1, 2, 3, 4, 5, 6]}
    return render(request, 'first/result.html', context)