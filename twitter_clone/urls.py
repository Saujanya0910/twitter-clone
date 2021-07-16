"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

from apps.core.views import *
from apps.feed.views import *
from apps.user_profile.views import *

from apps.feed.api import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', frontpage, name='frontpage'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),

    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('profile/<str:username>/followers/', followers, name='followers'),
    path('profile/<str:username>/followings/', followings, name='followings'),
    path('profile/<str:username>/follow/', follow_user, name='follow_user'),
    path('profile/<str:username>/unfollow/', unfollow_user, name='unfollow_user'),

    # apis
    path('api/add_tweet/', api_add_tweet, name='api_add_tweet'),
    path('api/add_like/', api_add_like, name='api_add_like')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # static files for dev server
