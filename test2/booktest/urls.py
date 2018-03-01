from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index2),
    url(r'^index/$', views.index),
    url(r'^index/(\d+)/$',views.index1,name='indexd'),
    url(r'^te/$',views.te),
    url(r'^te1/$',views.te1),
    url(r'^(\d+)/$',views.gethero),
    url(r'showtest/$',views.showtest),
]