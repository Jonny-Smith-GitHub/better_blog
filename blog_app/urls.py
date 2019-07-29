'''
Created on 2019年7月26日

@author: Jonny
'''

from django.urls.conf import path


from . import views 



urlpatterns=[
    path('index/', views.index,name='index_page'),
    path('article/<int:article_id>/',views.article_page,name='article_page'),
    path('edit/<int:article_id>/',views.edit_page,name='edit_page'),
    path('edit/action/',views.edit_action,name='edit_action')
]