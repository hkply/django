from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^selectBook/$',views.selectBook),
    url(r'area/$',views.area)
]