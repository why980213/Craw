# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from mycraw.models import Result

# Create your views here.


def see(request):
    return render(request, 'home.html')


def index(request):
    dic = []
    for i in Result.objects.all():
        dic.append(i)
    return render(request, 'result.html', {'dic': dic})
