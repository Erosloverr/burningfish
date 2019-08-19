from django.db import connection
from django.shortcuts import render

# Create your views here.

def get_conn():
    return connection, connection.cursor()


def index(request):
    conn, cur = get_conn()

    username = request.GET.get('username')
    context = {
        'username': username,
        'admin': 'liangzhuang',
        'info': {'phone':'18810927950',
                 'Email':'liangzh@weilaicheng.com'
        }
    }
    return render(request,'index.html',context=context)
