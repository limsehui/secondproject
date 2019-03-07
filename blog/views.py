from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'blog/home.html',{'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'details':details})


def new(request):
    return render(request, 'blog/new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))