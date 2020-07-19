from django.urls import path
from blogcrud import views
app_name='blogcrud'

urlpatterns=[
    path('',views.landingview,name='landingpage'),
    path('list-of-blogs',views.list_blog,name='listblogs'),
    path('blog-detail/<int:blog_id>/',views.blog_detail,name='blogdetail'),
]