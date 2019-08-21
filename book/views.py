from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db import connection
from random import random
from book.models import Book
# Create your views here.


def get_conn():
    return connection,connection.cursor()


def book(request):
    # conn, cur = get_conn()
    # cur.execute("select id,name,author from books")
    # book_data = cur.fetchall()
    data_list = Book.objects.all().values()
    return render(request, 'book_index.html',context={"book_data":data_list})


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    if request.method == 'POST':
        book_name = request.POST.get("name")
        author = request.POST.get("author")
        book = Book(name=book_name, author=author)
        book.save()
        # conn, cur = get_conn()
        # sql = """insert into books values(%s,'%s','%s')""" % (id, book_name, author)
        # print("sql: %s" %sql)
        # cur.execute(sql)
        # conn.commit()
        return redirect(reverse("book:index"))


def del_book(request, book_id):
    conn, cur = get_conn()
    cur.execute("delete from book_book where id = %s" % (book_id))
    conn.commit()
    book_data = data_list = Book.objects.all().values()
    return render(request, 'book_index.html', context={"book_data": book_data})


def book_detail(request, book_id):
    return HttpResponse("%s" % book_id)
