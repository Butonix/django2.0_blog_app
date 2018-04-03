"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import AboutView

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('post/<pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<pk>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<pk>/comment', views.add_comments_to_post, name= 'add_comments_to_post'),
    path('comment/<pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove', views.comment_remove, name='comment_remove'),
    path('post/<pk>/publish', views.post_publish.as_view(), name='post_publish'),
]
