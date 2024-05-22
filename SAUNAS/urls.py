"""
URL configuration for SAUNAS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from top import views as top
from login import views as login
from post import views as post
from my_page import views as my_page
from detil import views as detil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top.top_template, name='top_template'),
    path('login/', login.login_template, name='login_template'),
    path('post/', post.post_template, name='post_template'),
    path('my_page/', my_page.my_page_template, name='my_page_template'),
    path('detil/', detil.detil_template, name='detil_template')
]
