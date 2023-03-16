"""fotoblog URL Configuration

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
import authentication
from django.contrib import admin, messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.urls import path

import blog.views
from authentication.views import CustomPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('recovery-password/', PasswordResetView.as_view(
        template_name='authentication/recovery-password.html',
        success_url='/',
    ), name='recovery-password'),
    path('change-password/', CustomPasswordChangeView.as_view(
        template_name='blog/change-password.html',
        success_url='/home/',
    ), name='change-password'),
    path('home/', blog.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
]
