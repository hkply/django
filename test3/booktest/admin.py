
from django.contrib import admin
from models import *

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 3

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender','hcontent','hbook']
    list_filter = ['hname']
    search_fields = ['hname']
    list_per_page = 10
    fields = ['hname', 'hgender','hcontent','hbook']

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date','bread','bcomment','isDelete']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('super', {'fields': ['bpub_date']})
    ]
    inlines = [HeroInfoInline]



admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(BookInfo,BookInfoAdmin)