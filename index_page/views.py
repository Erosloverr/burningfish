from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    context = {
        'admin': 'liangzhuang',
        'info': {'phone':'18810927950',
                 'Email':'liangzh@weilaicheng.com'
        }
    }
    return render(request,'index.html',context=context)
