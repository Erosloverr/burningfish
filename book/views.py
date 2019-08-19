from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from random import random
# Create your views here.


def get_conn():
    return connection,connection.cursor()


def book(request):
    conn, cur = get_conn()
    cur.execute("select id,name,author from books")
    book_data = cur.fetchall()
    return render(request, 'book_index.html',context={"book_data":book_data})


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    if request.method == 'POST':
        id = int(random()*1000)
        conn, cur = get_conn()
        book_name = request.POST.get("name")
        author = request.POST.get("author")
        sql = """insert into books values(%s,'%s','%s')""" % (id, book_name, author)
        print("sql: %s" %sql)
        cur.execute(sql)
        conn.commit()
        return render(request, 'add_book.html')


def del_book(request,book_id):
    conn, cur = get_conn()
    cur.execute("delete from books where id = %s" %book_id)
    conn.commit()
    cur.execute("select id,name,author from books")
    book_data = cur.fetchall()
    return render(request, 'book_index.html', context={"book_data": book_data})


def book_detail(request, book_id):
    pass
