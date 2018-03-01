#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def index(request):
    return HttpResponse('hello django')

def index1(request,id):
    it=int(id)
    print type(id)
    return HttpResponse('id:%d'%it)
def index2(request):
    return HttpResponse('什么都没输入')

def te(request):
    return render(request,'booktest/te.html')

def te1(request):
    heroa=HeroInfo.objects.all()
    booklist=BookInfo.objects.all()
    context={'herolist':heroa,'booklist':booklist}
    return render(request,'booktest/te1.html',context)

def gethero(request,bookid):
    bid=int(bookid)
    book = BookInfo.objects.get(id=bid)
    herolist=book.heroinfo_set.all()
    context={'herolist':herolist}
    return render(request,'booktest/showhero.html',context)

def showtest(request):
    return HttpResponse('showtest')