from django.contrib import admin

from blog_app.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','title','content','pub_time')

admin.site.register(Article,ArticleAdmin)