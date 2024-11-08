from django.shortcuts import render, redirect
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})

def create_blog(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        category = request.POST['category']
        content = request.POST['content']
        Blog.objects.create(title=title, author=author, category=category, content=content)
        return redirect('blog-list')
    return render(request, 'create.html')
