from django.shortcuts import render
from django.contrib import admin
from  .models import Blog

admin.site.register(Blog) #블로그 형식을 가져와 등록하겠다.
# Create your views here.
def home(request):
  blogs = Blog.objects
  return render(request,'home.html',{'blogs':blogs})

