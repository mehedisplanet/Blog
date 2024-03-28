from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=['topic','title','body']

admin.site.register(Blog,BlogAdmin)