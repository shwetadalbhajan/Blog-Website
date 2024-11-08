from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("author","title")

admin.site.register(Blog,BlogAdmin)
