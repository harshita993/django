from django.contrib import admin
from news.models import News

class Newsadmin(admin.ModelAdmin):
    list_display=('news_title','news_description')
admin.site.register(News,Newsadmin)
