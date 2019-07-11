from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import admin #어드민 쓸꺼면 써야됨
from  .models import Blog #앱을 가지고 오겠다는거
from django.utils import timezone

admin.site.register(Blog) #블로그 형식을 가져와 등록하겠다.
# Create your views here.
def home(request):
  blogs = Blog.objects
  return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail= get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog': blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))