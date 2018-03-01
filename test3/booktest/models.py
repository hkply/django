#coding=utf-8
from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    bread=models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete=models.BooleanField(default=False)
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
