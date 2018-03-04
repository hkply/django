#coding=utf-8
from django.db import models

# Create your models here.

#新建模型类的管理器类
# class BookInfoManager(models.Manager):
#     def get_queryset(self):
#         return super(BookInfoManager,self).get_queryset().filter(isDelete=True)
#
#     def create(self,title,pub_date,read,comment,isdelete):
#         book=BookInfo()
#         book.btitle=title
#         book.bpub_date=pub_date
#         book.bread=read
#         book.bcomment=comment
#         book.isDelete=isdelete
#         return book




class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(null=True)
    bread=models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete=models.BooleanField(default=False)
    book1=models.Manager() #管理器objects用book1代替
    # book2=BookInfoManager()


    class Meta():
        db_table='bookinfo' #将数据库中的表改名为bookinfo,否则默认为应用名_类名(小写)
        ordering=['id'] #数据库中按id排序
    def __str__(self):
        return self.btitle.encode("utf-8")


class HeroInfo(models.Model):
   hname=models.CharField(max_length=20)
   hgender=models.BooleanField(default=False)
   isDelete=models.BooleanField(default=False)
   hcontent=models.CharField(max_length=20)
   hbook=models.ForeignKey(BookInfo)
   def __str__(self):
       return self.hname.encode("utf-8")


class Areas(models.Model):
    atitle = models.CharField(max_length=20)
    pid = models.ForeignKey('self', null=True, blank=True)

