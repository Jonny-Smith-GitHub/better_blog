'''
Created on 2019年7月26日

@author: Jonny
'''

from django.urls.conf import path

from . import views 


urlpatterns=[
    path('', views.index),
]