'''
Created on 2019年7月26日

@author: Jonny
'''

from django.urls.conf import path

from . import views 


urlpatterns=[
    path('index/', views.index),
    path('article/<int:article_id>/',views.article_page,name='article_page')
]