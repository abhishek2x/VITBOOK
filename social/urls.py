from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls.conf import include
from social import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('attendance/', views.attendance, name='attendance'),
    path('grades/', views.grades, name='grades'),

    path('chat/',  views.ChatView.as_view(), name='chat_ajax'),
    path('chat/create/',  views.CreateChatUser.as_view(), name='chat_ajax_create'),
    
    path('ub/', views.ub, name='ub'),
    path('ub/upload', views.Ubupload),

    path('contact/', views.ContactView, name='contact'),
    path('contact/upload', views.ContactViewUpload),
    path('developer/', views.JoinView, name='developer'),
    path('developer/upload', views.JoinViewUpload),
    path('home', RedirectView.as_view(url="/")),

    path('post/create/', views.MyPostCreate.as_view(success_url="/post"), name='postCreate'),
    path('post/delete/<int:pk>',
         views.MyPostDeleteView.as_view(success_url="/post"), name='postDelete'),

    path('post/', views.MyPostListView.as_view(), name='postList'),
    path('post/<int:pk>', views.MyPostDetailView.as_view(), name='postDetail'),
    path('post/like/<int:pk>/<page>', views.like, name="like"),
    path('post/unlike/<int:pk>/<page>', views.unlike, name='unlike'),

    path('profile/edit/<int:pk>',
         views.MyProfileUpdateView.as_view(success_url="/home"), name='profileEdit'),
    path('profile/', views.MyProfileListView.as_view(), name='profileList'),
    path('profile/<int:pk>', views.profiling, name='profileDetail'),


    path('profile/follow/<int:pk>', views.follow, name='follow'),
    path('profile/unfollow/<int:pk>', views.unfollow, name='unfollow'),

    path('vithub/create/', views.VithubCreate.as_view(success_url="/vithub"), name='vithubCreate'),
    path('vithub/delete/<int:pk>',
         views.VithubDeleteView.as_view(success_url="/vithub"), name='vithubDelete'),
    path('vithub/', views.VithubListView.as_view(), name='vithubList'),
    path('vithub/<int:pk>', views.VithubDetailView.as_view(), name='vithubDetail'),


    path('poll/', views.poll_home, name='poll_home'),
    path('poll/create/', views.poll_create, name='poll_create'),
    path('poll/vote/<poll_id>/', views.poll_vote, name='poll_vote'),
    path('poll/results/<poll_id>/', views.poll_results, name='poll_results'),


]
