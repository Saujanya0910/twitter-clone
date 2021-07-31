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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# views
from apps.core.views import frontpage, signup
from apps.feed.views import feed, search
from apps.user_profile.views import user_profile, edit_profile, follow_user, unfollow_user, followers, followings, tweet_likes
from apps.conversation.views import conversation, conversations
from apps.notification.views import notifications

# forms
from apps.user_profile.forms import UserLoginForm

# api endpoints
from apps.feed.api import api_add_tweet, api_add_like, api_delete_like
from apps.conversation.api import api_send_message


urlpatterns = [
    path('admin/', admin.site.urls),

    # auth views
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', redirect_authenticated_user=True, authentication_form=UserLoginForm), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='core/change_password.html',success_url='/'), name='change_password'),

    
    path('', frontpage, name='frontpage'),
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),

    path('tweet/likes/<int:tweet_id>/', tweet_likes, name='tweet_likes'),

    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('profile/<str:username>/followers/', followers, name='followers'),
    path('profile/<str:username>/followings/', followings, name='followings'),
    path('profile/<str:username>/follow/', follow_user, name='follow_user'),
    path('profile/<str:username>/unfollow/', unfollow_user, name='unfollow_user'),

    path('conversations/', conversations, name='conversations'),
    path('conversation/<int:user_id>/', conversation, name='conversation'),

    path('notifications/', notifications, name='notifications'),

    # api endpoints
    path('api/add_tweet/', api_add_tweet, name='api_add_tweet'),
    path('api/add_like/', api_add_like, name='api_add_like'),
    path('api/delete_like/', api_delete_like, name='api_delete_like'),
    path('api/send_message/', api_send_message, name='api_send_message')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # static files for dev server
