# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.blog_post_detail, name='post_detail'),
]
