"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

# Handles static files media and images
from django.conf import settings
from django.conf.urls.static import static

# User views
from django.contrib.auth import views as auth_views
from users import views as user_views
from posts import views as post_views

urlpatterns = [

    # Ajax comments and messages
    path('save-comment',post_views.save_comment,name='save-comment'),
    path('save-unlogged-comment',post_views.save_unlogged_comment,name='save-unlogged-comment'),
    
    # Ajax upvote
    # path('save-question-upvote',post_views.save_upvote,name='save-upvote'),

    path('', include('core.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('signup/', user_views.signup, name='signup'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)