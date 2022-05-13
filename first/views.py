from email import contentmanager
from http.client import HTTP_VERSION_NOT_SUPPORTED, ImproperConnectionState
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import date, datetime

import random

# 데이터를 꺼내와 화면에 나타내고 싶은 것들의 로직
def index(request):
    now = datetime.now()
    context = {
        'current_date' : now
    }    
    return render(request, 'first/index.html', context)


def select(request):
    context={}
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number']) #get으로 받아오는 값은 str

    results=[]
    if chosen >= 1 and chosen <= 45:
        result.append(chosen)
    
    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers': results
    }
    
    return render(request, 'first/result.html', context)