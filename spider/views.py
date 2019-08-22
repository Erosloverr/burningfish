from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
import os


# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'spider/index.html')
    if request.method == 'POST':
        r = os.popen("ps -ef | grep SpiderXuMing.py | wc -l")
        run_flag = r.read()
        r.close()
        if int(run_flag) >3:
            return HttpResponse("已经有一个爬虫程序再执行了！请耐心等待邮件！")
        else:
            cmd = "nohup python3 /home/burningfish/myProject/SpiderXuMing.py > /home/burningfish/myProject/spider_log/log.txt &"
            os.system(cmd)
            return HttpResponse("程序已经开始执行！请耐心等待邮件！")
