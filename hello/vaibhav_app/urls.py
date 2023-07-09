from django.contrib import admin
from django.urls import path,include
from vaibhav_app import views

urlpatterns = [
    
    path('',views.index,name='vaibhav_app'),
    
    path('about',views.about,name='vaibhav_app_about'),
    path('postComment', views.postComment, name="postComment"),
    path('post',views.post,name='vaibhav_app_post'),
    path('blog',views.blog,name='vaibhav_app_blog'),
    path('blog/<str:slug>', views.blogPost, name='blogPost'),
    
    
    path('contacts',views.contacts,name='vaibhav_app_contacts'),
    
    path('search', views.search, name="search"),
    path('signup', views.handleSignup, name="handleSignup"),

    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    

]