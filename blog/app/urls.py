from django.urls import path
from .views import blog_list, create_blog

urlpatterns = [
    path('', blog_list, name='blog-list'),
    path('create/', create_blog, name='create-blog'),
]