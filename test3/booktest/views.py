#conding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse
from django.db.models import Q,F


# Create your views here.
def index(request):
    return render(request,'booktest/index.html')

def selectBook(request):
    # return HttpResponse('fsdfsdf')
    book1=BookInfo.book1.all()
    bookcount=book1.count()
    list = BookInfo.book1.filter(heroinfo__hgender =0)
    list2=BookInfo.book1.filter(bread__gte=F('bcomment'))
    book2 = BookInfo.book1.filter(bread=34)
    context={'book1':book1,'book2':book2,'list':list,'list2':list2,'bookcount':bookcount}
    return render(request,'booktest/book.html',context)

def area(request):  #有错误 ,数据库中已存入数据
    # return HttpResponse('fsdfsdf')
    area = Areas.objects.get(id__lt=100)
    return render(request, 'booktest/area.html', {'area': area})