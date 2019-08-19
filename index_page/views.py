from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    cursor = connection.cursor()
    SQL = "select count(*) from orders"
    cursor.execute(SQL)
    rows = cursor.fetchone()
    data_rows = rows[0]
    username = request.GET.get('username')
    context = {
        'data_rows': data_rows,
        'username': username,
        'admin': 'liangzhuang',
        'info': {'phone':'18810927950',
                 'Email':'liangzh@weilaicheng.com'
        }
    }
    return render(request,'index.html',context=context)
