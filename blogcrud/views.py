from django.shortcuts import render
from .models import Blogs,Aurthor
# Create your views here.
def landingview(request):
    return render(request,'index.html')

def list_blog(request):
    blog_list=Blogs.objects.all()
    context = {
        'blog_list':blog_list,
    }
    return render(request,'bloglist.html',context)

def blog_detail(request,blog_id):
    get_blog=Blogs.objects.get(id=blog_id)
    context={
        'blogdetail':get_blog
    }
    return  render(request,'detailblog.html',context)
