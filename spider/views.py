from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
import os


# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'spider/index.html')
    if request.method == 'POST':
        cmd = "python3 /home/burningfish/myProject/optimize_spider_v2.py >> /home/burningfish/myProject/spider_log/log.txt &"
        os.system(cmd)
        return HttpResponse("程序已经开始执行！请耐心等待邮件！")