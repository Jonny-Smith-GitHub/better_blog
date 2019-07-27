from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    articles=models.Article.objects.all()
    return render(request, "blog_app/index.html",{'articles':articles})
