# views.py
from django.shortcuts import render
from .models import BlogPost



def blog_post_detail(request, post_id):
    

    return render(request, 'blog_detail.html')
